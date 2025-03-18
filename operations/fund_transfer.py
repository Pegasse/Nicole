import os
import json
import logging
from datetime import date, datetime
import requests
from config import Config, logger

logger = logging.getLogger(__name__)

class FundTransferHandler:
    """Processes internal fund transfers between accounts."""
    
    def __init__(self, token_manager):
        self.token_manager = token_manager
        # Get all cash and bank accounts
        self.cash_bank_accounts = self.token_manager.get_asset_accounts()
        # Create dictionaries for quick lookups
        self.account_by_id = {acc["account_id"]: acc for acc in self.cash_bank_accounts}
        self.account_by_name = {acc["account_name"].lower(): acc for acc in self.cash_bank_accounts}
        logger.info(f"Fund Transfer Handler initialized with {len(self.cash_bank_accounts)} cash and bank accounts")
        
        # Dictionary of common account names and their variations for more flexible matching
        self.common_account_names = {
            "expense provisions": ["expense provisions", "expense provision", "expenses provisions", "provisions", "expense account"],
            "mc cash": ["mc cash", "microconcept cash", "microconcepts cash", "micro concept cash"],
            "mc bank": ["mc bank", "microconcept bank", "microconcepts bank", "micro concept bank"],
            "be cash": ["be cash", "bellissima cash", "bellissimas cash"],
            "be bank": ["be bank", "bellissima bank", "bellissimas bank"],
            "mcasie cash": ["mcasie cash", "mc asie cash", "mcasie", "purchasing office cash"],
            "cash in transit": ["cash in transit", "transit", "transit cash", "in transit"],
            "buying petty cash": ["buying petty cash", "petty cash", "buying cash", "petty"]
        }
        
    def _find_account(self, account_name_or_id):
        """Find an account by name or ID"""
        if not account_name_or_id:
            return None
        
        # Check if it's an ID
        if account_name_or_id in self.account_by_id:
            account = self.account_by_id[account_name_or_id]
            return account
        
        # Check if exact lowercase name match
        if account_name_or_id.lower() in self.account_by_name:
            account = self.account_by_name[account_name_or_id.lower()]
            return account
        
        # Try partial matching on names
        for name, account in self.account_by_name.items():
            if account_name_or_id.lower() in name:
                logger.info(f"Found partial match for account: {account_name_or_id} → {name}")
                return account
        
        # No matches found
        return None
    
    def process(self, data, sender_name=""):
        """Process a fund transfer request"""
        logger.info(f"Processing fund transfer: {data}")
        
        # Validate required fields
        for field in ["amount", "from_account", "to_account"]:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return {
                    "status": "error",
                    "text": f"Missing {field} in the request",
                    "data": data
                }
        
        # Ensure amount is positive
        try:
            amount = float(data["amount"])
            if amount <= 0:
                logger.error(f"Invalid amount: {amount}")
                return {
                    "status": "error",
                    "text": "Amount must be a positive number",
                    "data": data
                }
        except (ValueError, TypeError):
            logger.error(f"Invalid amount format: {data['amount']}")
            return {
                "status": "error",
                "text": f"Invalid amount format: {data['amount']}",
                "data": data
            }
            
        # Get accounts
        from_account = self._find_account(data["from_account"])
        to_account = self._find_account(data["to_account"])
        
        # Check if accounts are found
        if not from_account:
            logger.error(f"Source account not found: {data['from_account']}")
            alternatives = self._get_account_alternatives()
            return {
                "status": "error",
                "text": f"Source account '{data['from_account']}' not found. Available accounts: {alternatives}",
                "data": data
            }
            
        if not to_account:
            logger.error(f"Destination account not found: {data['to_account']}")
            alternatives = self._get_account_alternatives()
            return {
                "status": "error",
                "text": f"Destination account '{data['to_account']}' not found. Available accounts: {alternatives}",
                "data": data
            }
            
        # Same account check
        if from_account["account_id"] == to_account["account_id"]:
            logger.error(f"Cannot transfer to the same account: {from_account['account_name']}")
            return {
                "status": "error",
                "text": f"Cannot transfer to the same account: {from_account['account_name']}",
                "data": data
            }
            
        # Handle special case for MCAsie/Cash In Transit
        if to_account and to_account.get('account_name', '').lower() == 'mcasie cash':
            # Look for Cash In Transit account
            for name, account in self.account_by_name.items():
                if 'cash in transit' in name:
                    to_account = account
                    logger.info(f"Converting destination to Cash In Transit for MCAsie transfer")
                    break
        
        # Get display names for accounts
        from_display_name = from_account.get('account_name', data['from_account'])
        to_display_name = to_account.get('account_name', data['to_account'])
        
        purpose = data.get("reference", "Funds Transfer")
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
                    "account_id": to_account["account_id"],
                    "debit_amount": amount,
                    "credit_amount": 0
                },
                {
                    "account_id": from_account["account_id"],
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
                
    def _get_account_alternatives(self):
        """Get a list of available account names as a formatted string"""
        if not self.cash_bank_accounts:
            return "No cash or bank accounts available"
            
        account_names = [acc["account_name"] for acc in self.cash_bank_accounts]
        return ", ".join(account_names) 