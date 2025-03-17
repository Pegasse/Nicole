import os
import json
from datetime import date, datetime
import logging
import requests
from config import Config, logger
from utils.message_sender import CliqMessageSender

logger = logging.getLogger(__name__)

class FundTransferHandler:
    """Handles fund transfer operations"""
    
    def __init__(self, token_manager):
        """Initialize the handler with token manager"""
        self.token_manager = token_manager
        self.cliq_sender = CliqMessageSender()
        
        # Load account IDs from config
        self.account_ids = {
            # Primary account IDs
            'mc_cash': Config.MC_CASH_ID,
            'mc_bank': Config.MC_BANK_ID,
            'mc_mpesa': Config.MC_MPESA_ID,
            'be_cash': Config.BE_CASH_ID,
            'be_bank': Config.BE_BANK_ID,
            'be_mpesa': Config.BE_MPESA_ID,
            'mcasie_cash': Config.MCASIE_CASH_ID,
            'cash_in_transit': Config.CASH_IN_TRANSIT_ID,
            'royalties_available': Config.ROYALTIES_AVAILABLE_ID,
            'expense_provisions': Config.EXPENSE_PROVISIONS_ID,
            'fond_de_caisse': Config.FOND_DE_CAISSE_ID,
            'buying_petty_cash': Config.BUYING_PETTY_CASH_ID
        }
        
        # Account name variations mapping to standard names
        self.account_name_map = {
            # MC variations
            'microconcept': 'mc_cash',
            'microconcept_cash': 'mc_cash',
            'microconcept_bank': 'mc_bank',
            'microconcept_mpesa': 'mc_mpesa',
            
            # BE variations
            'bellissima': 'be_cash',
            'bellissima_cash': 'be_cash',
            'bellissima_bank': 'be_bank',
            'bellissima_mpesa': 'be_mpesa',
            'belli': 'be_cash',
            'belli_cash': 'be_cash',
            'belli_bank': 'be_bank',
            'belli_mpesa': 'be_mpesa',
            
            # MCAsie variations
            'mcasie': 'mcasie_cash',
            'asie': 'mcasie_cash',
            'rac': 'mcasie_cash',
            
            # Other variations
            'transit': 'cash_in_transit',
            'royalties': 'royalties_available',
            'provisions': 'expense_provisions',
            'fond': 'fond_de_caisse',
            'caisse': 'fond_de_caisse',
            'petty_cash': 'buying_petty_cash',
            'buying_petty': 'buying_petty_cash'
        }
        
        # If any account IDs are missing, log a warning
        missing_accounts = [k for k, v in self.account_ids.items() if not v]
        if missing_accounts:
            logger.warning(f"Missing account IDs for: {', '.join(missing_accounts)}")
    
    def process(self, parsed_data, sender_name):
        """Process a fund transfer request"""
        try:
            # Ensure we have a valid token
            self.token_manager.ensure_valid_token()
            
            # Extract transfer details
            amount = parsed_data.get('amount')
            from_account = parsed_data.get('from_account', '').lower()
            to_account = parsed_data.get('to_account', '').lower()
            
            # Validate accounts
            if not from_account or not to_account:
                response_text = f"@{sender_name}: Please specify both 'from' and 'to' accounts for the transfer."
                # Send the message but don't fail if message sending fails
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "message": response_text, "amount": amount, "from_account": from_account, "to_account": to_account}
            
            # Original account names for display
            original_from = from_account
            original_to = to_account
            
            # Normalize account names using the mapping
            from_account = self.normalize_account_name(from_account)
            to_account = self.normalize_account_name(to_account)
            
            # Get account IDs
            from_account_id = self.account_ids.get(from_account)
            to_account_id = self.account_ids.get(to_account)
            
            if not from_account_id or not to_account_id:
                invalid_accounts = []
                if not from_account_id:
                    invalid_accounts.append(f"'{original_from}'")
                if not to_account_id:
                    invalid_accounts.append(f"'{original_to}'")
                
                invalid_msg = " and ".join(invalid_accounts)
                
                # Log what was attempted and what was available
                logger.error(f"Invalid account(s): {invalid_msg}")
                logger.error(f"Normalized from: '{original_from}' -> '{from_account}', to: '{original_to}' -> '{to_account}'")
                logger.error(f"Available accounts: {', '.join(sorted(self.account_ids.keys()))}")
                logger.error(f"Available mappings: {self.account_name_map}")
                
                response_text = f"@{sender_name}: Invalid account name(s): {invalid_msg}. Please use one of these accounts: {', '.join(sorted(set(self.account_ids.keys())))}"
                
                # Send the message but don't fail if message sending fails
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "message": response_text, "amount": amount, "from_account": original_from, "to_account": original_to}
            
            # Execute the transfer
            result = self.execute_transfer(amount, from_account_id, to_account_id)
            
            # Send success message, but don't fail if message sending fails
            response_text = f"@{sender_name}: Successfully transferred {amount} from {original_from} to {original_to}"
            self.cliq_sender.send_message("Nicole", response_text)
            
            # Return successful result
            return {
                "status": "success", 
                "message": response_text, 
                "amount": amount, 
                "from_account": original_from, 
                "to_account": original_to
            }
            
        except Exception as e:
            error_message = f"Error processing transfer: {str(e)}"
            logger.error(error_message, exc_info=True)
            
            # Try to send error message, but don't fail if message sending fails
            response_text = f"@{sender_name}: {error_message}"
            try:
                self.cliq_sender.send_message("Nicole", response_text)
            except Exception as msg_error:
                logger.error(f"Failed to send error message: {str(msg_error)}")
            
            # Return error result with all the information we have
            return {
                "status": "error", 
                "message": error_message, 
                "amount": parsed_data.get('amount'), 
                "from_account": parsed_data.get('from_account', ''), 
                "to_account": parsed_data.get('to_account', '')
            }
    
    def execute_transfer(self, amount, from_account_id, to_account_id):
        """Execute the fund transfer in Zoho Books"""
        try:
            # Format the date and reference number like in old_brain.py
            current_date = date.today().isoformat()
            reference_number = f"TRANSFER-{date.today().strftime('%Y%m%d')}-{int(datetime.now().timestamp()) % 10000}"
            
            # Prepare the transfer payload exactly like in old_brain.py
            payload = {
                "date": current_date,
                "from_account_id": from_account_id,
                "to_account_id": to_account_id,
                "amount": amount,
                "reference_number": reference_number,
                "description": f"Transfer of {amount} between accounts",
                "transaction_type": "transfer_fund"  # This field was missing in our implementation
            }
            
            logger.info(f"Executing transfer: {from_account_id} to {to_account_id} for amount {amount}")
            
            # Make the API request
            response = self._execute_transaction(payload)
            
            if response.status_code >= 400:
                try:
                    error_data = response.json()
                    error_message = error_data.get('message', 'Unknown error')
                except:
                    error_message = f"Status code: {response.status_code}, Response: {response.text}"
                    
                raise Exception(f"Zoho Books API Error: {error_message}")
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Error executing transfer: {str(e)}")
            raise
    
    def _execute_transaction(self, payload):
        """Execute the API call to Zoho Books"""
        # Use the correct API URL format from old_brain.py
        base_url = "https://www.zohoapis.com/books/v3"
        org_id = Config.ZOHO_ORG_ID
        
        if not org_id:
            logger.error("Missing ZOHO_ORG_ID environment variable")
            raise Exception("Zoho organization ID is missing")
            
        url = f"{base_url}/banktransactions?organization_id={org_id}"
        
        logger.info(f"Executing transaction to URL: {url}")
        logger.info(f"Payload: {json.dumps(payload)}")
        
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
            "Content-Type": "application/json"
        }
        
        logger.info(f"Using token: {self.token_manager.get_token()[:10]}...")
        
        response = requests.post(url, json=payload, headers=headers)
        
        logger.info(f"Response status: {response.status_code}")
        logger.info(f"Response body: {response.text[:200]}")
        
        return response
    
    def normalize_account_name(self, account_name):
        """Normalize account names to standard format"""
        account_name = account_name.lower().strip()
        
        # Check if the account name is already a standard name
        if account_name in self.account_ids:
            return account_name
            
        # Check if it's a known variation
        if account_name in self.account_name_map:
            return self.account_name_map[account_name]
            
        # If not found, return the original name
        return account_name 