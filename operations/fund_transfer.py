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
                return {"status": "error", "text": response_text, "amount": amount, "from_account": from_account, "to_account": to_account}
            
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
                return {"status": "error", "text": response_text, "amount": amount, "from_account": original_from, "to_account": original_to}
            
            # Execute the transfer
            result = self.execute_transfer(amount, from_account_id, to_account_id)
            
            # Extract transaction IDs for the message
            transaction_ids = []
            if "first_transaction" in result:
                # Try to get the transaction ID from the JSON response
                first_transaction = result.get("first_transaction", {})
                if "banktransaction" in first_transaction:
                    transaction_ids.append(first_transaction["banktransaction"].get("transaction_id", "Unknown"))
                elif "banktransfer" in first_transaction:
                    transaction_ids.append(first_transaction["banktransfer"].get("banktransfer_id", "Unknown"))
                
            if "second_transaction" in result:
                # Try to get the transaction ID from the JSON response
                second_transaction = result.get("second_transaction", {})
                if "banktransaction" in second_transaction:
                    transaction_ids.append(second_transaction["banktransaction"].get("transaction_id", "Unknown"))
                elif "banktransfer" in second_transaction:
                    transaction_ids.append(second_transaction["banktransfer"].get("banktransfer_id", "Unknown"))
            
            # If no transaction IDs were found, check for direct transaction
            if not transaction_ids and "banktransaction" in result:
                transaction_ids.append(result["banktransaction"].get("transaction_id", "Unknown"))
            elif not transaction_ids and "banktransfer" in result:
                transaction_ids.append(result["banktransfer"].get("banktransfer_id", "Unknown"))
            
            # Join transaction IDs for display
            transaction_id_text = " and ".join(transaction_ids) if transaction_ids else "N/A"
            
            # Send success message, but don't fail if message sending fails
            if "second_transaction" in result:
                # This was a two-step transfer
                response_text = f"@{sender_name}: Successfully transferred ${amount} from {original_from} to {original_to} via Cash In Transit. Transaction ID(s): {transaction_id_text}"
            else:
                response_text = f"@{sender_name}: Successfully transferred ${amount} from {original_from} to {original_to}. Transaction ID: {transaction_id_text}"
                
            # Send the success message to Nicole channel - using same channel as old_brain.py
            self.cliq_sender.send_message("Nicole", response_text)
            
            # For MCAsie transfers, also send a notification to recipient like in old_brain.py
            to_mcasie = any(key == to_account and 'mcasie' in key.lower() for key in self.account_ids.keys())
            is_cash_in_transit = to_account == 'cash_in_transit'
            if to_mcasie or is_cash_in_transit:
                recipient_msg = f"RAC: {sender_name} sent ${amount} from {original_from} to {original_to}. Please confirm receipt."
                self.cliq_sender.send_message("Nicole", recipient_msg)  # old_brain.py also sent to "Nicole" channel
            
            # Return successful result with transaction info - matching old_brain.py format
            return {
                "status": "success", 
                "text": response_text,  # change from "message" to "text" to match old_brain.py
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
            
            # Return error result matching old_brain.py format
            return {
                "status": "error", 
                "text": response_text,  # change to "text" to match old_brain.py
                "amount": parsed_data.get('amount'), 
                "from_account": parsed_data.get('from_account', ''), 
                "to_account": parsed_data.get('to_account', '')
            }
    
    def execute_transfer(self, amount, from_account_id, to_account_id):
        """Execute the fund transfer in Zoho Books using Cash In Transit as intermediary"""
        try:
            # Format the date and reference number like in old_brain.py
            current_date = date.today().isoformat()
            reference_number = f"TRANSFER-{date.today().strftime('%Y%m%d')}-{int(datetime.now().timestamp()) % 10000}"
            
            # Get Cash In Transit account ID
            cash_in_transit_id = Config.CASH_IN_TRANSIT_ID
            
            if not cash_in_transit_id:
                raise Exception("Cash In Transit account ID is missing")
            
            logger.info(f"Executing transfer: {from_account_id} to {to_account_id} for amount {amount} via Cash In Transit")
                
            # Check if this is a transfer to/from MCAsie
            is_mcasie_transfer = any(value == to_account_id for key, value in self.account_ids.items() if 'mcasie' in key.lower())
            
            # For MCAsie transfers, we can try a direct transfer
            if is_mcasie_transfer and cash_in_transit_id == to_account_id:
                logger.info(f"Direct transfer to Cash In Transit")
                return self._execute_single_transaction(amount, from_account_id, to_account_id, current_date, reference_number)
            
            # For all other transfers, use the two-transaction approach
            logger.info(f"Using two-transaction approach via Cash In Transit")
            
            # First transaction: from_account to Cash In Transit
            first_payload = {
                "date": current_date,
                "from_account_id": from_account_id,
                "to_account_id": cash_in_transit_id,
                "amount": amount,
                "reference_number": reference_number,
                "description": f"Transfer of {amount} (Part 1: Source to Cash In Transit)",
                "transaction_type": "transfer_fund"
            }
            
            logger.info(f"Executing first transaction: {from_account_id} to {cash_in_transit_id}")
            first_response = self._execute_transaction(first_payload)
            
            if first_response.status_code >= 400:
                try:
                    error_data = first_response.json()
                    error_message = error_data.get('message', 'Unknown error')
                except:
                    error_message = f"Status code: {first_response.status_code}, Response: {first_response.text}"
                    
                raise Exception(f"First transaction failed: {error_message}")
            
            # Second transaction: Cash In Transit to to_account
            second_payload = {
                "date": current_date,
                "from_account_id": cash_in_transit_id,
                "to_account_id": to_account_id,
                "amount": amount,
                "reference_number": f"{reference_number}-2",
                "description": f"Transfer of {amount} (Part 2: Cash In Transit to Destination)",
                "transaction_type": "transfer_fund"
            }
            
            logger.info(f"Executing second transaction: {cash_in_transit_id} to {to_account_id}")
            second_response = self._execute_transaction(second_payload)
            
            if second_response.status_code >= 400:
                try:
                    error_data = second_response.json()
                    error_message = error_data.get('message', 'Unknown error')
                except:
                    error_message = f"Status code: {second_response.status_code}, Response: {second_response.text}"
                    
                raise Exception(f"Second transaction failed: {error_message}")
            
            # Both transactions succeeded
            result = {
                "first_transaction": first_response.json(),
                "second_transaction": second_response.json()
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error executing transfer: {str(e)}")
            raise
            
    def _execute_single_transaction(self, amount, from_account_id, to_account_id, current_date, reference_number):
        """Execute a single direct transaction between accounts"""
        payload = {
            "date": current_date,
            "from_account_id": from_account_id,
            "to_account_id": to_account_id,
            "amount": amount,
            "reference_number": reference_number,
            "description": f"Direct transfer of {amount} between accounts",
            "transaction_type": "transfer_fund"
        }
        
        response = self._execute_transaction(payload)
        
        if response.status_code >= 400:
            try:
                error_data = response.json()
                error_message = error_data.get('message', 'Unknown error')
            except:
                error_message = f"Status code: {response.status_code}, Response: {response.text}"
                
            raise Exception(f"Direct transaction failed: {error_message}")
        
        return response.json()
    
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