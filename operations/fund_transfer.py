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
        self.cash_bank_accounts = []
        self.refresh_accounts()  # Call refresh_accounts instead of directly fetching in init
        
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
        
    def refresh_accounts(self):
        """Refresh account information from Zoho Books"""
        try:
            # Get asset accounts
            self.cash_bank_accounts = self.token_manager.get_asset_accounts()
            logger.info(f"Refreshed {len(self.cash_bank_accounts)} cash and bank accounts from Zoho Books")
            
            # Create dictionaries for quick lookups
            self.account_by_id = {acc["account_id"]: acc for acc in self.cash_bank_accounts} if self.cash_bank_accounts else {}
            self.account_by_name = {}
            
            # Create case-insensitive lookup by name
            for acc in self.cash_bank_accounts:
                if "account_name" in acc and acc["account_name"]:
                    name_lower = acc["account_name"].lower()
                    self.account_by_name[name_lower] = acc
                    
                    # Log account names for debugging
                    logger.debug(f"Added account to lookup: {acc['account_name']} (ID: {acc['account_id']})")
            
            logger.info(f"Created lookups with {len(self.account_by_id)} ID entries and {len(self.account_by_name)} name entries")
        except Exception as e:
            logger.error(f"Error refreshing accounts: {str(e)}")
            # Don't clear accounts on error to avoid losing existing data
        
    def _find_account(self, account_name_or_id):
        """Find an account by name or ID"""
        if not account_name_or_id:
            return None
        
        account_name_lower = account_name_or_id.lower() if account_name_or_id else ""
        logger.info(f"Searching for account: '{account_name_or_id}'")
        
        # Check if it's an ID
        if account_name_or_id in self.account_by_id:
            logger.info(f"Found account by exact ID match: {account_name_or_id}")
            return self.account_by_id[account_name_or_id]
            
        # Check if exact lowercase name match
        if account_name_lower in self.account_by_name:
            logger.info(f"Found account by exact lowercase name match: {account_name_lower}")
            return self.account_by_name[account_name_lower]
        
        # Log account name map for debugging
        logger.debug(f"Account name map keys: {list(self.account_by_name.keys())}")
        
        # Try common name variations from our dictionary
        matched_common_name = None
        for common_name, variations in self.common_account_names.items():
            if account_name_lower in variations or common_name in account_name_lower:
                logger.info(f"Found match through common name variations: {account_name_or_id} → {common_name}")
                matched_common_name = common_name
                break
        
        if matched_common_name:
            # Look for this common_name in our Zoho accounts
            for name_key, account in self.account_by_name.items():
                # Try different matching strategies
                if matched_common_name in name_key:
                    logger.info(f"Matched common name {matched_common_name} to account {name_key}")
                    return account
                    
                # Check for specific keywords like "cash" or "bank"
                if ("cash" in matched_common_name and "cash" in name_key) or ("bank" in matched_common_name and "bank" in name_key):
                    logger.info(f"Matched by type (cash/bank): {matched_common_name} to account {name_key}")
                    return account
        
        # Try partial matching on names
        best_match = None
        best_match_score = 0
        
        for name_key, account in self.account_by_name.items():
            # If account name contains the search term
            if account_name_lower in name_key:
                logger.info(f"Found partial match (search in key): {account_name_or_id} → {name_key}")
                if len(account_name_lower) > best_match_score:
                    best_match = account
                    best_match_score = len(account_name_lower)
                    
            # If the search term contains the account name
            elif name_key in account_name_lower:
                logger.info(f"Found reverse partial match (key in search): {name_key} in {account_name_or_id}")
                if len(name_key) > best_match_score:
                    best_match = account
                    best_match_score = len(name_key)
                    
            # Try matching on key words (cash, bank, etc.)
            if "cash" in account_name_lower and "cash" in name_key:
                logger.info(f"Keyword match on 'cash': {account_name_or_id} → {name_key}")
                best_match = account
                best_match_score = max(best_match_score, 5)  # Assign a reasonable score
                
            if "bank" in account_name_lower and "bank" in name_key:
                logger.info(f"Keyword match on 'bank': {account_name_or_id} → {name_key}")
                best_match = account
                best_match_score = max(best_match_score, 5)  # Assign a reasonable score
        
        if best_match:
            logger.info(f"Returning best partial match with score {best_match_score}")
            return best_match
        
        # No matches found
        logger.warning(f"No account match found for: {account_name_or_id}")
        logger.warning(f"Available account names: {list(self.account_by_name.keys())}")
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
        
        # Debug information about available accounts before matching
        logger.info(f"Number of cash/bank accounts available: {len(self.cash_bank_accounts)}")
        logger.info(f"Number of accounts in account_by_name map: {len(self.account_by_name)}")
        logger.info(f"Available account names: {[acc.get('account_name', 'unnamed') for acc in self.cash_bank_accounts]}")
        
        # If accounts list is empty, try refreshing
        if not self.cash_bank_accounts:
            logger.warning("No accounts found in handler, attempting to refresh accounts")
            self.refresh_accounts()
            
            if not self.cash_bank_accounts:
                logger.error("Still no accounts after refresh. Zoho Books may not be returning accounts.")
                return {
                    "status": "error",
                    "text": "Could not retrieve any cash or bank accounts from Zoho Books. Please check your configuration and ensure accounts exist.",
                    "data": data
                }
                    
        # Get accounts
        from_account = self._find_account(data["from_account"])
        to_account = self._find_account(data["to_account"])
        
        # Debug account matching
        logger.info(f"Available accounts: {[acc['account_name'] for acc in self.cash_bank_accounts]}")
        logger.info(f"Looking for from_account: {data['from_account']}, found: {from_account['account_name'] if from_account else 'None'}")
        logger.info(f"Looking for to_account: {data['to_account']}, found: {to_account['account_name'] if to_account else 'None'}")
        
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
        
        # Log account IDs for debugging
        logger.info(f"Using source account: {from_account['account_name']} with ID: {from_account['account_id']}")
        logger.info(f"Using destination account: {to_account['account_name']} with ID: {to_account['account_id']}")
        
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
        
        # Create a unique reference number for the transaction
        reference_number = f"TRANSFER-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Get current date in YYYY-MM-DD format
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Get display names for accounts
        from_display_name = from_account.get('account_name', data['from_account'])
        to_display_name = to_account.get('account_name', data['to_account'])
        
        purpose = data.get("reference", "Funds Transfer")
        description = f"Transfer from {from_display_name} to {to_display_name}" 
        if purpose:
            description += f" - {purpose}"
            
        # Set up the API endpoint and headers
        url = f"{Config.ZOHO_API_URL}/banktransactions?organization_id={Config.ZOHO_ORG_ID}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
            "Content-Type": "application/json"
        }
        
        # Format the amount as a string with 2 decimal places
        formatted_amount = "{:.2f}".format(amount)
        
        # Prepare the bank transfer transaction payload
        payload = {
            "date": current_date,
            "account_id": from_account["account_id"],
            "transaction_type": "transfer_fund",
            "reference_number": reference_number,
            "amount": formatted_amount,
            "to_account_id": to_account["account_id"],
            "description": description
        }
        
        # Log the payload for debugging
        logger.info(f"Sending bank transfer payload to Zoho: {json.dumps(payload)}")
        
        # Make the API request
        response = requests.post(url, headers=headers, json=payload)
        
        # Log the complete response for debugging
        logger.info(f"Zoho API response: Status {response.status_code}, Response: {response.text}")
        
        # Check if the request was successful
        if response.status_code in [200, 201]:
            result = response.json()
            logger.info(f"Transaction created successfully: {result}")
            # Return success response
            return {
                "status": "success",
                "text": f"✅ Transfer completed successfully!\nAmount: {amount}\nFrom: {from_display_name}\nTo: {to_display_name}",
                "data": result
            }
        else:
            # Handle error
            try:
                error_data = response.json()
                error_msg = error_data.get("message", "Unknown error")
                error_code = error_data.get("code", 0)
                
                logger.error(f"API Error ({response.status_code}): {response.text}")
                return {
                    "status": "error",
                    "text": f"❌ Transfer failed: {error_msg}",
                    "data": error_data
                }
            except Exception as e:
                error_msg = f"Error processing response: {str(e)}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
                
    def _get_account_alternatives(self):
        """Get a list of available account names as a formatted string"""
        if not self.cash_bank_accounts:
            return "No cash or bank accounts available. Please ensure Zoho Books is properly configured with cash or bank accounts."
            
        account_names = [acc["account_name"] for acc in self.cash_bank_accounts]
        if not account_names:
            return "No named accounts available. Please check your Zoho Books configuration."
            
        return ", ".join(account_names) 