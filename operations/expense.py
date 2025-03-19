import logging
from datetime import date
import requests
import re
from config import Config, logger
import json

class ExpenseHandler:
    """Handler for processing expense entries"""
    
    def __init__(self, token_manager):
        """Initialize with the token manager"""
        self.token_manager = token_manager
        # Get expense accounts
        self.expense_accounts = self.token_manager.get_expense_accounts()
        # Get cash and bank accounts
        self.cash_bank_accounts = self.token_manager.get_asset_accounts()
        
        # Get available currencies
        self.currencies = self.token_manager.get_currencies()
        # Store currency details for quick lookup
        self.currency_by_code = {}
        self.currency_by_symbol = {}
        self.currency_by_name = {}
        
        # Process currencies for lookup
        self._process_currencies()
        
        # Create lookup dictionaries - ensure we don't crash if accounts are empty
        self.expense_account_by_id = {acc["account_id"]: acc for acc in self.expense_accounts} if self.expense_accounts else {}
        self.expense_account_by_name = {acc["account_name"].lower(): acc for acc in self.expense_accounts} if self.expense_accounts else {}
        
        self.payment_account_by_id = {acc["account_id"]: acc for acc in self.cash_bank_accounts} if self.cash_bank_accounts else {}
        self.payment_account_by_name = {acc["account_name"].lower(): acc for acc in self.cash_bank_accounts} if self.cash_bank_accounts else {}
        
        # Dictionary of common payment account names and variations for flexible matching
        self.common_payment_accounts = {
            "expense provisions": ["expense provisions", "expense provision", "expenses provisions", "provisions", "expense account"],
            "mc cash": ["mc cash", "microconcept cash", "microconcepts cash", "micro concept cash"],
            "be cash": ["be cash", "bellissima cash", "bellissimas cash"],
            "buying petty cash": ["buying petty cash", "petty cash", "buying cash", "petty"]
        }
        
        logger.info(f"Expense Handler initialized with {len(self.expense_accounts)} expense accounts, {len(self.cash_bank_accounts)} payment accounts, and {len(self.currencies)} currencies")
        # Initialize account mappings
        self.refresh_accounts()
    
    def _process_currencies(self):
        """Process the currencies from Zoho for easy lookup"""
        if not self.currencies:
            logger.warning("No currencies fetched from Zoho. Will default to USD.")
            # Add a default USD entry
            self.currency_by_code["USD"] = {"currency_code": "USD", "currency_symbol": "$", "currency_name": "US Dollar", "currency_id": "USD"}
            self.currency_by_symbol["$"] = {"currency_code": "USD", "currency_symbol": "$", "currency_name": "US Dollar", "currency_id": "USD"}
            self.currency_by_name["us dollar"] = {"currency_code": "USD", "currency_symbol": "$", "currency_name": "US Dollar", "currency_id": "USD"}
            return
            
        for currency in self.currencies:
            code = currency.get("currency_code", "")
            symbol = currency.get("currency_symbol", "")
            name = currency.get("currency_name", "")
            
            if code:
                self.currency_by_code[code] = currency
            if symbol:
                self.currency_by_symbol[symbol] = currency
            if name:
                self.currency_by_name[name.lower()] = currency
                
        logger.info(f"Processed {len(self.currency_by_code)} currency codes, {len(self.currency_by_symbol)} symbols, and {len(self.currency_by_name)} names")
        
    def _detect_currency(self, text, amount_str):
        """Detect currency from text and amount string.
        Returns a tuple (currency_info, cleaned_amount_value, was_detected) where:
        - currency_info contains currency details if found
        - cleaned_amount_value is the amount without currency symbols
        - was_detected is a boolean indicating if a currency was explicitly detected
        """
        # Default currency info (only used if no currency is detected)
        default_currency = {"currency_code": "USD"}
        
        if not text and not amount_str:
            return default_currency, 0, False
            
        # First check if there's a currency symbol in the amount
        if amount_str:
            # Remove commas from amount for processing
            amount_str = amount_str.replace(",", "")
            # Check for currency symbols
            for symbol in self.currency_by_symbol:
                if symbol in amount_str:
                    currency = self.currency_by_symbol[symbol]
                    # Remove the symbol to get clean amount
                    clean_amount = amount_str.replace(symbol, "").strip()
                    logger.info(f"Detected currency {currency.get('currency_code')} from symbol {symbol} in amount {amount_str}")
                    return currency, clean_amount, True
        
        # Check for currency codes in the text (USD, EUR, etc.)
        if text:
            # Look for 3-letter currency codes
            currency_codes = re.findall(r'\b([A-Z]{3})\b', text.upper())
            for code in currency_codes:
                if code in self.currency_by_code:
                    currency = self.currency_by_code[code]
                    logger.info(f"Detected currency code {code} in text")
                    return currency, amount_str, True
                    
            # Look for currency names in the text
            text_lower = text.lower()
            for name, currency in self.currency_by_name.items():
                if name in text_lower:
                    logger.info(f"Detected currency {currency.get('currency_code')} from name {name} in text")
                    return currency, amount_str, True
        
        # If no currency detected, default to USD without setting currency_id
        logger.info(f"No currency detected in text or amount, defaulting to USD but omitting currency_id")
        return default_currency, amount_str, False

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
                        name_lower = account_name.lower()
                        self.expense_account_map[name_lower] = account
                        logger.debug(f"Added expense account to lookup: {account_name} (ID: {account_id})")
            
            # Map asset accounts by ID and name
            for account in self.asset_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name', '')
                if account_id:
                    self.asset_account_map[account_id] = account
                    if account_name:
                        name_lower = account_name.lower()
                        self.asset_account_map[name_lower] = account
                        logger.debug(f"Added asset account to lookup: {account_name} (ID: {account_id})")
            
            # Log some sample account names for debugging
            if self.asset_accounts:
                asset_names = [acc.get('account_name', 'unnamed') for acc in self.asset_accounts[:3]]
                logger.info(f"Sample asset account names: {asset_names}")
                
            if self.expense_accounts:
                expense_names = [acc.get('account_name', 'unnamed') for acc in self.expense_accounts[:3]]
                logger.info(f"Sample expense account names: {expense_names}")
                        
            logger.info(f"Mapped {len(self.asset_account_map)} asset accounts and {len(self.expense_account_map)} expense accounts")
        except Exception as e:
            logger.error(f"Error refreshing accounts: {str(e)}")
            # Don't clear accounts on error to avoid losing existing data if partial fetch was successful

    def process(self, parsed_data, sender_name):
        """Process the parsed expense data and create an expense in Zoho Books."""
        try:
            # Extract and validate expense account ID
            account_id = parsed_data.get("account_id")
            account_name = parsed_data.get("account_name", "")
            
            # If account_id not provided but account_name is, try to find the account ID
            if not account_id and account_name:
                # Try exact match first
                if account_name.lower() in self.expense_account_map:
                    account = self.expense_account_map[account_name.lower()]
                    account_id = account.get('account_id')
                # Try partial match
                else:
                    for name, account in self.expense_account_map.items():
                        if isinstance(name, str) and account_name.lower() in name:
                            account_id = account.get('account_id')
                            logger.info(f"Found partial match for expense account: {account_name} → {name}")
                            break
                
                if account_id:
                    logger.info(f"Resolved expense account ID {account_id} from name {account_name}")
            
            # Validate we have an account ID
            if not account_id:
                alternatives = ", ".join([acc.get('account_name', '') for acc in self.expense_accounts[:10]])
                error_msg = f"Could not find expense account: {account_name}"
                if alternatives:
                    error_msg += f". Available accounts: {alternatives}"
                else:
                    error_msg += ". No expense accounts available - please ensure Zoho Books is properly configured."
                
                return {
                    "status": "error", 
                    "text": error_msg
                }
            
            # Extract and process amount with currency
            amount_str = str(parsed_data.get("amount", "0"))
            original_notes = parsed_data.get("notes", "")
            reference = parsed_data.get("reference", "Expense")
            
            # Extract currency code if provided directly in the parsed data
            parsed_currency = parsed_data.get("currency", "")
            
            # Detect currency from text and amount string
            all_text = f"{reference} {original_notes} {parsed_currency}"
            currency_info, cleaned_amount, currency_detected = self._detect_currency(all_text, amount_str)
            
            # Get currency details
            currency_code = currency_info.get("currency_code", "USD")  
            currency_id = currency_info.get("currency_id")
            
            # Log currency details for debugging
            if currency_detected and currency_id:
                logger.info(f"Using detected currency: Code={currency_code}, ID={currency_id}")
            else:
                logger.info(f"No specific currency detected, will use organization default")
            
            # Convert cleaned amount to float
            try:
                amount = float(cleaned_amount)
            except ValueError:
                # If conversion fails, remove any non-numeric characters except decimal point
                cleaned_amount = re.sub(r'[^\d.]', '', cleaned_amount)
                try:
                    amount = float(cleaned_amount)
                except ValueError:
                    logger.error(f"Could not parse amount from {amount_str}")
                    return {
                        "status": "error",
                        "text": f"Could not determine the expense amount from '{amount_str}'"
                    }
            
            # Other expense details
            date_str = parsed_data.get("date", date.today().isoformat())
            notes = f"{original_notes}\nCurrency: {currency_code}" if original_notes else f"Currency: {currency_code}"
            
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
            
            # If still no payment account and we have asset accounts, use the first one
            if not paid_through_account and self.asset_accounts:
                paid_through_account = self.asset_accounts[0]
                paid_through_id = paid_through_account.get('account_id')
                logger.info(f"Using first available asset account for payment: {paid_through_account.get('account_name')}")
            
            # If no payment account was found, return a descriptive error
            if not paid_through_id:
                alternatives = ", ".join([acc.get('account_name', '') for acc in self.asset_accounts[:10]])
                error_msg = f"Could not find a valid payment account"
                if alternatives:
                    error_msg += f". Available payment accounts: {alternatives}"
                else:
                    error_msg += ". No payment accounts available - please ensure Zoho Books is properly configured with cash or bank accounts."
                
                return {
                    "status": "error", 
                    "text": error_msg
                }
            
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
            
            # Only add currency_id if a currency was explicitly detected
            if currency_detected and currency_id:
                payload["currency_id"] = currency_id
                
            # Add paid_through_account_id if available
            if paid_through_id:
                payload["paid_through_account_id"] = paid_through_id
            
            # Log the payload for debugging
            logger.info(f"Sending expense payload to Zoho: {json.dumps(payload)}")
                    
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
                
                # Create success message with currency information
                currency_text = f"{currency_code} " if currency_detected else ""
                
                if paid_through_name:
                    response_text = f"✅ Successfully recorded expense of {currency_text}{amount} to {display_account_name} paid through {paid_through_name}. Expense ID: {expense_id}"
                else:
                    response_text = f"✅ Successfully recorded expense of {currency_text}{amount} to {display_account_name}. Expense ID: {expense_id}"
                
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