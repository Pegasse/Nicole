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
        
        # Find the transit account
        transit_account = None
        for acc in self.cash_bank_accounts:
            if 'transit' in acc.get('account_name', '').lower() or 'in transit' in acc.get('account_name', '').lower():
                transit_account = acc
                logger.info(f"Found transit account: {transit_account['account_name']}")
                break
                
        # If no transit account found, look for Cash In Transit specifically
        if not transit_account:
            for name, account in self.account_by_name.items():
                if 'cash in transit' in name.lower():
                    transit_account = account
                    logger.info(f"Found Cash In Transit account: {transit_account['account_name']}")
                    break
                    
        # If still no transit account, create an error
        if not transit_account:
            logger.error("No transit account found for double transfer")
            return {
                "status": "error",
                "text": "No transit account found. Please create a 'Cash In Transit' account in Zoho Books.",
                "data": data
            }
                
        # Create a unique reference number for the transactions
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        reference_number_1 = f"TRANSFER1-{timestamp}"
        reference_number_2 = f"TRANSFER2-{timestamp}"
        
        # Get current date in YYYY-MM-DD format
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Get display names for accounts
        from_display_name = from_account.get('account_name', data['from_account'])
        transit_display_name = transit_account.get('account_name', 'Transit Account')
        to_display_name = to_account.get('account_name', data['to_account'])
        
        purpose = data.get("reference", "Funds Transfer")
        description_1 = f"Transfer from {from_display_name} to {transit_display_name} (Step 1 of 2)"
        description_2 = f"Transfer from {transit_display_name} to {to_display_name} (Step 2 of 2)"
        if purpose:
            description_1 += f" - {purpose}"
            description_2 += f" - {purpose}"
            
        # Ensure token is valid
        if not self.token_manager.ensure_valid_token():
            return {"status": "error", "text": "Failed to refresh Zoho API token"}
            
        # Set up the API endpoint and headers
        url = f"{Config.ZOHO_API_URL}/banktransactions?organization_id={Config.ZOHO_ORG_ID}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
            "Content-Type": "application/json"
        }
        
        # Format the amount as a string with 2 decimal places
        formatted_amount = "{:.2f}".format(amount)
        
        # -------------------- FIRST TRANSFER: Source to Transit --------------------
        # Prepare the first bank transfer transaction payload
        payload_1 = {
            "date": current_date,
            "account_id": from_account["account_id"],
            "transaction_type": "transfer_fund",
            "reference_number": reference_number_1,
            "amount": formatted_amount,
            "to_account_id": transit_account["account_id"],
            "description": description_1
        }
        
        # Log the payload for debugging
        logger.info(f"Sending first bank transfer payload to Zoho: {json.dumps(payload_1)}")
        
        # Make the first API request
        response_1 = requests.post(url, headers=headers, json=payload_1)
        
        # Log the complete response for debugging
        logger.info(f"Zoho API response for first transfer: Status {response_1.status_code}, Response: {response_1.text}")
        
        # Check if the first request was successful
        if response_1.status_code not in [200, 201]:
            # Handle error
            try:
                error_data = response_1.json()
                error_msg = error_data.get("message", "Unknown error")
                logger.error(f"First transfer failed: {error_msg}")
                return {
                    "status": "error",
                    "text": f"❌ First transfer failed: {error_msg}",
                    "data": error_data
                }
            except Exception as e:
                error_msg = f"Error processing response: {str(e)}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
                
        # -------------------- SECOND TRANSFER: Transit to Destination --------------------
        # Prepare the second bank transfer transaction payload
        payload_2 = {
            "date": current_date,
            "account_id": transit_account["account_id"],
            "transaction_type": "transfer_fund",
            "reference_number": reference_number_2,
            "amount": formatted_amount,
            "to_account_id": to_account["account_id"],
            "description": description_2
        }
        
        # Log the payload for debugging
        logger.info(f"Sending second bank transfer payload to Zoho: {json.dumps(payload_2)}")
        
        # Make the second API request
        response_2 = requests.post(url, headers=headers, json=payload_2)
        
        # Log the complete response for debugging
        logger.info(f"Zoho API response for second transfer: Status {response_2.status_code}, Response: {response_2.text}")
        
        # Check if the second request was successful
        if response_2.status_code not in [200, 201]:
            # The first transfer succeeded but second failed, we should handle this case
            logger.error("First transfer succeeded but second failed")
            
            try:
                error_data = response_2.json()
                error_msg = error_data.get("message", "Unknown error")
                logger.error(f"Second transfer failed: {error_msg}")
                return {
                    "status": "error",
                    "text": f"❌ Warning: First transfer to transit account succeeded, but second transfer failed: {error_msg}. Manual intervention required.",
                    "data": error_data
                }
            except Exception as e:
                error_msg = f"Error processing response: {str(e)}"
                logger.error(error_msg)
                return {"status": "error", "text": f"❌ Warning: First transfer succeeded, but second transfer failed. Manual intervention required. Error: {error_msg}"}
        
        # Both transfers succeeded
        try:
            result_1 = response_1.json()
            result_2 = response_2.json()
            
            # Return success response
            logger.info(f"Double transfer completed successfully")
            return {
                "status": "success",
                "text": f"✅ Transfer completed successfully!\nAmount: {amount}\nFrom: {from_display_name}\nVia: {transit_display_name}\nTo: {to_display_name}",
                "data": {
                    "first_transfer": result_1,
                    "second_transfer": result_2
                }
            }
        except Exception as e:
            logger.error(f"Error processing successful transfers: {str(e)}")
            # Both transfers likely succeeded but we couldn't parse the responses
            return {
                "status": "success",
                "text": f"✅ Transfer appears successful but couldn't process response. Amount: {amount} from {from_display_name} to {to_display_name} via {transit_display_name}",
                "data": {
                    "first_response": response_1.text,
                    "second_response": response_2.text
                }
            }
                
    def _get_account_alternatives(self):
        """Get a list of available account names as a formatted string"""
        if not self.cash_bank_accounts:
            return "No cash or bank accounts available. Please ensure Zoho Books is properly configured with cash or bank accounts."
            
        account_names = [acc["account_name"] for acc in self.cash_bank_accounts]
        if not account_names:
            return "No named accounts available. Please check your Zoho Books configuration."
            
        return ", ".join(account_names) 