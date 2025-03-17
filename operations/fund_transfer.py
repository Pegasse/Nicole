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
            'cash_in_transit': Config.CASH_IN_TRANSIT_ACCOUNT,
            'be_bank': Config.BE_BANK_ACCOUNT,
            'bellissima': Config.BELLISSIMA_BANK_ACCOUNT,
            'mcasie': Config.MCASIE_BANK_ACCOUNT,
            'bdms': Config.BDMS_BANK_ACCOUNT
        }
    
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
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "text": response_text}
            
            # Get account IDs
            from_account_id = self.account_ids.get(from_account)
            to_account_id = self.account_ids.get(to_account)
            
            if not from_account_id or not to_account_id:
                response_text = f"@{sender_name}: Invalid account name(s). Valid accounts are: {', '.join(self.account_ids.keys())}"
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "text": response_text}
            
            # Execute the transfer
            result = self.execute_transfer(amount, from_account_id, to_account_id)
            
            # Send success message
            response_text = f"@{sender_name}: Successfully transferred {amount} from {from_account} to {to_account}"
            self.cliq_sender.send_message("Nicole", response_text)
            return {"status": "success", "text": response_text}
            
        except Exception as e:
            error_message = f"Error processing transfer: {str(e)}"
            logger.error(error_message, exc_info=True)
            response_text = f"@{sender_name}: {error_message}"
            self.cliq_sender.send_message("Nicole", response_text)
            return {"status": "error", "text": error_message}
    
    def execute_transfer(self, amount, from_account_id, to_account_id):
        """Execute the fund transfer in Zoho Books"""
        try:
            # Prepare the transfer payload
            payload = {
                "from_account_id": from_account_id,
                "to_account_id": to_account_id,
                "amount": amount,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "reference_number": f"AUTO-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            }
            
            # Make the API request
            response = self._execute_transaction(payload)
            
            if response.status_code != 201:
                error_data = response.json()
                raise Exception(f"Zoho Books API Error: {error_data.get('message', 'Unknown error')}")
            
            return response.json()
            
        except Exception as e:
            logger.error(f"Error executing transfer: {str(e)}")
            raise
    
    def _execute_transaction(self, payload):
        """Execute the API call to Zoho Books"""
        url = "https://books.zoho.com/api/v3/banktransfers"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
            "Content-Type": "application/json"
        }
        
        return requests.post(url, json=payload, headers=headers) 