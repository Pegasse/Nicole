import logging
from datetime import date
import requests
from config import Config, logger

class ExpenseHandler:
    def __init__(self, token_manager):
        self.token_manager = token_manager
        # Initialize account mappings
        self.refresh_accounts()
    
    def refresh_accounts(self):
        """Refresh account information from Zoho Books"""
        try:
            # Get asset accounts for payment accounts
            self.asset_accounts = self.token_manager.get_asset_accounts()
            logger.info(f"Loaded {len(self.asset_accounts)} asset accounts from Zoho Books")
            
            # Get expense accounts
            self.expense_accounts = self.token_manager.get_expense_accounts()
            logger.info(f"Loaded {len(self.expense_accounts)} expense accounts from Zoho Books")
            
            # Create maps for easy lookup
            self.expense_account_map = {}
            self.asset_account_map = {}
            
            # Map expense accounts by ID and normalized name
            for account in self.expense_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name', '')
                if account_id:
                    self.expense_account_map[account_id] = account
                    # Also map by normalized name (lowercase with underscores)
                    if account_name:
                        normalized_key = account_name.lower().replace(' ', '_')
                        self.expense_account_map[normalized_key] = account
            
            # Map asset accounts by ID and normalized name
            for account in self.asset_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name', '')
                if account_id:
                    self.asset_account_map[account_id] = account
                    # Also map by normalized name (lowercase with underscores)
                    if account_name:
                        normalized_key = account_name.lower().replace(' ', '_')
                        self.asset_account_map[normalized_key] = account
                        
            logger.info(f"Mapped {len(self.asset_account_map)} asset accounts and {len(self.expense_account_map)} expense accounts")
        except Exception as e:
            logger.error(f"Error refreshing accounts: {str(e)}")
            self.asset_accounts = []
            self.expense_accounts = []
            self.asset_account_map = {}
            self.expense_account_map = {}

    def process(self, parsed_data, sender_name):
        """Process the parsed expense data and create an expense in Zoho Books."""
        try:
            # Extract and validate expense account ID
            account_id = parsed_data.get("account_id")
            account_name = parsed_data.get("account_name", "")
            
            # If account_id not provided but account_name is, try to find the account ID
            if not account_id and account_name and account_name in self.expense_account_map:
                account = self.expense_account_map[account_name]
                account_id = account.get('account_id')
                logger.info(f"Resolved account ID {account_id} from name {account_name}")
            
            # Validate we have an account ID
            if not account_id:
                return {
                    "status": "error", 
                    "text": f"Could not find expense account: {account_name}"
                }
            
            # Extract other expense details
            amount = float(parsed_data["amount"])
            date_str = parsed_data.get("date", date.today().isoformat())
            reference = parsed_data.get("reference", "Expense")
            notes = parsed_data.get("notes", "")
            
            # Handle paid_through account (payment account)
            paid_through = parsed_data.get("paid_through", "")
            paid_through_account = None
            
            # Try to resolve paid_through to an asset account
            if paid_through:
                # Check if it's an ID or name
                if paid_through in self.asset_account_map:
                    paid_through_account = self.asset_account_map[paid_through]
                else:
                    # Try normalized variations
                    normalized_paid_through = paid_through.lower().replace(' ', '_')
                    if normalized_paid_through in self.asset_account_map:
                        paid_through_account = self.asset_account_map[normalized_paid_through]
            
            # If we didn't find the account, log a warning but continue
            if not paid_through_account and paid_through:
                logger.warning(f"Could not find payment account: {paid_through}")
            
            # Ensure token is valid
            if not self.token_manager.ensure_valid_token():
                return {"status": "error", "text": "Failed to refresh Zoho API token"}
            
            # Prepare API request
            headers = {
                "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
                "Content-Type": "application/json"
            }
            
            url = f"{Config.ZOHO_API_URL}/expenses?organization_id={Config.ZOHO_ORG_ID}"
            
            # Build payload
            payload = {
                "account_id": account_id,
                "amount": amount,
                "date": date_str,
                "reference_number": reference,
                "description": notes
            }
            
            # Add paid_through_account_id if available
            if paid_through_account:
                paid_through_id = paid_through_account.get('account_id')
                if paid_through_id:
                    payload["paid_through_account_id"] = paid_through_id
                    
            # Make the API request
            response = requests.post(url, headers=headers, json=payload)
            
            if response.status_code == 201:
                # Process successful response
                result = response.json()
                expense_id = result.get("expense", {}).get("expense_id", "Unknown")
                
                # Get account name for display
                display_account_name = account_name
                if not display_account_name and account_id in self.expense_account_map:
                    display_account_name = self.expense_account_map[account_id].get('account_name', 'Unknown')
                
                # Get paid through account name for display
                paid_through_name = ""
                if paid_through_account:
                    paid_through_name = paid_through_account.get('account_name', '')
                
                # Create success message
                if paid_through_name:
                    response_text = f"@{sender_name}: Successfully recorded expense of ${amount} to {display_account_name} paid through {paid_through_name}. Expense ID: {expense_id}"
                else:
                    response_text = f"@{sender_name}: Successfully recorded expense of ${amount} to {display_account_name}. Expense ID: {expense_id}"
                
                logger.info(response_text)
                return {"status": "success", "text": response_text}
            else:
                error_msg = f"API Error ({response.status_code}): {response.text}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
        except Exception as e:
            error_msg = f"Error processing expense: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "text": error_msg}