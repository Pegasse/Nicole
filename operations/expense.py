import logging
from datetime import date
import requests
from config import Config, logger

class ExpenseHandler:
    """Handler for processing expense entries"""
    
    def __init__(self, token_manager):
        """Initialize with the token manager"""
        self.token_manager = token_manager
        # Get expense accounts
        self.expense_accounts = self.token_manager.get_expense_accounts()
        # Get cash and bank accounts
        self.cash_bank_accounts = self.token_manager.get_asset_accounts()
        
        # Create lookup dictionaries
        self.expense_account_by_id = {acc["account_id"]: acc for acc in self.expense_accounts}
        self.expense_account_by_name = {acc["account_name"].lower(): acc for acc in self.expense_accounts}
        
        self.payment_account_by_id = {acc["account_id"]: acc for acc in self.cash_bank_accounts}
        self.payment_account_by_name = {acc["account_name"].lower(): acc for acc in self.cash_bank_accounts}
        
        # Dictionary of common payment account names and variations for flexible matching
        self.common_payment_accounts = {
            "expense provisions": ["expense provisions", "expense provision", "expenses provisions", "provisions", "expense account"],
            "mc cash": ["mc cash", "microconcept cash", "microconcepts cash", "micro concept cash"],
            "be cash": ["be cash", "bellissima cash", "bellissimas cash"],
            "buying petty cash": ["buying petty cash", "petty cash", "buying cash", "petty"]
        }
        
        logger.info(f"Expense Handler initialized with {len(self.expense_accounts)} expense accounts and {len(self.cash_bank_accounts)} payment accounts")
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
            
            # Create maps for direct ID and name lookup
            self.expense_account_map = {}
            self.asset_account_map = {}
            
            # Map expense accounts by ID and name
            for account in self.expense_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name', '')
                if account_id:
                    self.expense_account_map[account_id] = account
                    if account_name:
                        self.expense_account_map[account_name.lower()] = account
            
            # Map asset accounts by ID and name
            for account in self.asset_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name', '')
                if account_id:
                    self.asset_account_map[account_id] = account
                    if account_name:
                        self.asset_account_map[account_name.lower()] = account
                        
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
            if not account_id and account_name:
                # Try exact match first
                if account_name in self.expense_account_map:
                    account = self.expense_account_map[account_name]
                    account_id = account.get('account_id')
                # Try lowercase match
                elif account_name.lower() in self.expense_account_map:
                    account = self.expense_account_map[account_name.lower()]
                    account_id = account.get('account_id')
                
                if account_id:
                    logger.info(f"Resolved expense account ID {account_id} from name {account_name}")
            
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
            paid_through_id = None
            
            # Try to resolve paid_through to an asset account
            if paid_through:
                # Check if it's an ID directly
                if paid_through in self.asset_account_map:
                    paid_through_account = self.asset_account_map[paid_through]
                    paid_through_id = paid_through
                # Try by name (lowercase)
                elif paid_through.lower() in self.asset_account_map:
                    paid_through_account = self.asset_account_map[paid_through.lower()]
                    paid_through_id = paid_through_account.get('account_id')
                # Try to find it by name
                else:
                    # Look for partial matches
                    for acc_name, acc in self.asset_account_map.items():
                        if isinstance(acc_name, str) and paid_through.lower() in acc_name.lower():
                            paid_through_account = acc
                            paid_through_id = acc.get('account_id')
                            logger.info(f"Found partial match for payment account: {paid_through} → {acc_name}")
                            break
            
            # If we didn't find a payment account, look for an account named 'Expense Provisions'
            if not paid_through_account:
                for acc in self.asset_accounts:
                    if acc.get('account_name', '').lower() == 'expense provisions':
                        paid_through_account = acc
                        paid_through_id = acc.get('account_id')
                        logger.info(f"Using default 'Expense Provisions' account for payment")
                        break
            
            # If still no payment account, use the first asset account if available
            if not paid_through_account and self.asset_accounts:
                paid_through_account = self.asset_accounts[0]
                paid_through_id = paid_through_account.get('account_id')
                logger.info(f"Using first available asset account for payment: {paid_through_account.get('account_name')}")
            
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

    def _get_payment_account_alternatives(self):
        """Get a list of available payment account names as a formatted string"""
        if not self.cash_bank_accounts:
            return "No cash or bank accounts available"
            
        account_names = [acc["account_name"] for acc in self.cash_bank_accounts]
        return ", ".join(account_names)