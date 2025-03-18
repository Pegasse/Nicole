import os
import json
import logging
from datetime import date, datetime
import requests
from config import Config, logger

logger = logging.getLogger(__name__)

class FundTransferHandler:
    """Handles fund transfer operations"""
    
    def __init__(self, token_manager):
        """Initialize with necessary dependencies"""
        self.token_manager = token_manager
        
        # Load accounts from Zoho when initialized
        self.refresh_accounts()
        
    def refresh_accounts(self):
        """Refresh account information from Zoho Books"""
        try:
            # Get asset accounts from Zoho
            self.asset_accounts = self.token_manager.get_asset_accounts()
            logger.info(f"Loaded {len(self.asset_accounts)} asset accounts from Zoho Books")
            
            # Create direct lookup maps by ID and name
            self.account_by_id = {}
            self.account_by_name = {}
            
            # Populate account maps from Zoho data
            for account in self.asset_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name')
                
                if account_id and account_name:
                    self.account_by_id[account_id] = account
                    self.account_by_name[account_name.lower()] = account
            
            logger.info(f"Mapped {len(self.account_by_id)} accounts for fund transfers")
        except Exception as e:
            logger.error(f"Error refreshing accounts: {str(e)}")
            self.asset_accounts = []
            self.account_by_id = {}
            self.account_by_name = {}
    
    def _find_account(self, account_name_or_id):
        """Find an account by name or ID"""
        if not account_name_or_id:
            return None, None
        
        # Check if it's an ID
        if account_name_or_id in self.account_by_id:
            account = self.account_by_id[account_name_or_id]
            return account, account.get('account_id')
        
        # Check if exact lowercase name match
        if account_name_or_id.lower() in self.account_by_name:
            account = self.account_by_name[account_name_or_id.lower()]
            return account, account.get('account_id')
        
        # Try partial matching on names
        for name, account in self.account_by_name.items():
            if account_name_or_id.lower() in name:
                logger.info(f"Found partial match for account: {account_name_or_id} → {name}")
                return account, account.get('account_id')
        
        # No matches found
        return None, None
    
    def process(self, parsed_data, sender_name):
        """Process a fund transfer request"""
        # Extract data from parsed result
        try:
            amount = float(parsed_data.get("amount", 0))
            
            # Get account names/IDs
            from_account_name = parsed_data.get("from_account", "")
            to_account_name = parsed_data.get("to_account", "")
            
            # Find accounts by name or ID
            from_account, from_account_id = self._find_account(from_account_name)
            to_account, to_account_id = self._find_account(to_account_name)
            
            # Handle special case for MCAsie/Cash In Transit
            if to_account and to_account.get('account_name', '').lower() == 'mcasie cash':
                # Look for Cash In Transit account
                for name, account in self.account_by_name.items():
                    if 'cash in transit' in name:
                        to_account = account
                        to_account_id = account.get('account_id')
                        logger.info(f"Converting destination to Cash In Transit for MCAsie transfer")
                        break
            
            # Validate accounts exist
            if not from_account_id:
                return {"status": "error", "text": f"Source account not found: {from_account_name}"}
            
            if not to_account_id:
                return {"status": "error", "text": f"Destination account not found: {to_account_name}"}
            
            # Get display names for accounts
            from_display_name = from_account.get('account_name', from_account_name)
            to_display_name = to_account.get('account_name', to_account_name)
            
            purpose = parsed_data.get("reference", "Funds Transfer")
            description = f"Transfer from {from_display_name} to {to_display_name}" 
            if purpose:
                description += f" for {purpose}"
            
            # Ensure the token is valid
            if not self.token_manager.ensure_valid_token():
                return {"status": "error", "text": "Failed to refresh Zoho API token"}
            
            # Common transaction parameters
            current_date = date.today().isoformat()
            reference_number = f"TRANSFER-{date.today().strftime('%Y%m%d')}-{int(datetime.now().timestamp()) % 10000}"
            
            # Create the API request headers
            headers = {
                "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
                "Content-Type": "application/json"
            }
            
            # Create the journal entry
            url = f"{Config.ZOHO_API_URL}/journals?organization_id={Config.ZOHO_ORG_ID}"
            
            # Prepare the request payload
            payload = {
                "journal_date": current_date,
                "reference_number": reference_number,
                "notes": description,
                "line_items": [
                    {
                        "account_id": to_account_id,
                        "debit_amount": amount,
                        "credit_amount": 0
                    },
                    {
                        "account_id": from_account_id,
                        "debit_amount": 0,
                        "credit_amount": amount
                    }
                ]
            }
            
            # Make the API request
            response = requests.post(url, headers=headers, json=payload)
            
            # Check if the request was successful
            if response.status_code == 201:
                result = response.json()
                journal_id = result.get("journal", {}).get("journal_id", "Unknown")
                response_text = f"@{sender_name}: Successfully transferred ${amount} from {from_display_name} to {to_display_name}. Journal ID: {journal_id}"
                
                # Log the success
                logger.info(response_text)
                
                return {
                    "status": "success", 
                    "text": response_text,
                    "amount": amount,
                    "from_account": from_display_name,
                    "to_account": to_display_name
                }
            else:
                # Log and return the error
                error_msg = f"API Error ({response.status_code}): {response.text}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
                
        except Exception as e:
            # Log and return any exceptions
            error_msg = f"Error processing fund transfer: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "text": error_msg} 