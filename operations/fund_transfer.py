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
            asset_accounts = self.token_manager.get_asset_accounts()
            logger.info(f"Loaded {len(asset_accounts)} asset accounts from Zoho Books")
            
            # Create a map of account names to IDs
            self.account_ids = {}
            self.account_display_names = {}
            
            # Populate account maps from Zoho data
            for account in asset_accounts:
                account_id = account.get('account_id')
                account_name = account.get('account_name')
                
                if account_id and account_name:
                    # Create normalized key (lowercase with underscores)
                    normalized_key = account_name.lower().replace(' ', '_')
                    self.account_ids[normalized_key] = account_id
                    self.account_display_names[normalized_key] = account_name
            
            # Add legacy account mappings for backward compatibility
            self._add_legacy_account_mappings()
            
            # Create mapping to normalize account names from parsed data
            self.account_name_map = self._create_account_name_map()
            
            logger.info(f"Mapped {len(self.account_ids)} accounts for fund transfers")
        except Exception as e:
            logger.error(f"Error refreshing accounts: {str(e)}")
            # Fall back to hardcoded account IDs from Config
            self._initialize_fallback_accounts()
    
    def _add_legacy_account_mappings(self):
        """Add legacy account mappings for backward compatibility"""
        legacy_mappings = {
            "mc_cash": Config.MC_CASH_ID,
            "mc_bank": Config.MC_BANK_ID,
            "mc_mpesa": Config.MC_MPESA_ID,
            "be_cash": Config.BE_CASH_ID,
            "be_bank": Config.BE_BANK_ID,
            "be_mpesa": Config.BE_MPESA_ID,
            "mcasie_cash": Config.MCASIE_CASH_ID,
            "cash_in_transit": Config.CASH_IN_TRANSIT_ID,
            "royalties_available": Config.ROYALTIES_AVAILABLE_ID,
            "expense_provisions": Config.EXPENSE_PROVISIONS_ID,
            "fond_de_caisse": Config.FOND_DE_CAISSE_ID,
            "buying_petty_cash": Config.BUYING_PETTY_CASH_ID
        }
        
        legacy_display_names = {
            "mc_cash": "MC Cash",
            "mc_bank": "MC Bank",
            "mc_mpesa": "MC Mpesa",
            "be_cash": "BE Cash",
            "be_bank": "BE Bank", 
            "be_mpesa": "BE Mpesa",
            "mcasie_cash": "MCAsie Cash",
            "cash_in_transit": "Cash In Transit",
            "royalties_available": "Royalties Available",
            "expense_provisions": "Expense Provisions",
            "fond_de_caisse": "Fond de Caisse",
            "buying_petty_cash": "Buying Petty Cash"
        }
        
        # Add legacy mappings only if they don't already exist
        for key, value in legacy_mappings.items():
            if key not in self.account_ids and value:
                self.account_ids[key] = value
                self.account_display_names[key] = legacy_display_names.get(key, key.replace('_', ' ').title())
    
    def _create_account_name_map(self):
        """Create mapping to normalize account names"""
        account_map = {}
        
        # Add entries for all account display names
        for key, display_name in self.account_display_names.items():
            # Add regular form
            account_map[display_name.lower()] = key
            # Add with spaces replaced by underscores
            account_map[display_name.lower().replace(' ', '_')] = key
            # Add without spaces
            account_map[display_name.lower().replace(' ', '')] = key
            
        # Add common variations
        common_variations = {
            "mc cash": "mc_cash",
            "mc bank": "mc_bank",
            "mc mpesa": "mc_mpesa",
            "microconcept cash": "mc_cash",
            "microconcept bank": "mc_bank",
            "microconcept mpesa": "mc_mpesa",
            
            "be cash": "be_cash",
            "be bank": "be_bank",
            "be mpesa": "be_mpesa",
            "bellissima cash": "be_cash",
            "bellissima bank": "be_bank",
            "bellissima mpesa": "be_mpesa",
            
            "mcasie cash": "mcasie_cash",
            "rac": "mcasie_cash",
            "asie": "mcasie_cash",
            
            "cash in transit": "cash_in_transit",
            "royalties available": "royalties_available",
            "expense provisions": "expense_provisions",
            "fond de caisse": "fond_de_caisse",
            "buying petty cash": "buying_petty_cash"
        }
        
        # Add the common variations if their targets exist in account_ids
        for variation, target in common_variations.items():
            if target in self.account_ids:
                account_map[variation] = target
                
        return account_map
    
    def _initialize_fallback_accounts(self):
        """Initialize with fallback hardcoded account IDs"""
        logger.warning("Using fallback account IDs from Config")
        
        # Map internal names to account IDs from Config
        self.account_ids = {
            "mc_cash": Config.MC_CASH_ID,
            "mc_bank": Config.MC_BANK_ID,
            "mc_mpesa": Config.MC_MPESA_ID,
            "be_cash": Config.BE_CASH_ID,
            "be_bank": Config.BE_BANK_ID,
            "be_mpesa": Config.BE_MPESA_ID,
            "mcasie_cash": Config.MCASIE_CASH_ID,
            "cash_in_transit": Config.CASH_IN_TRANSIT_ID,
            "royalties_available": Config.ROYALTIES_AVAILABLE_ID,
            "expense_provisions": Config.EXPENSE_PROVISIONS_ID,
            "fond_de_caisse": Config.FOND_DE_CAISSE_ID,
            "buying_petty_cash": Config.BUYING_PETTY_CASH_ID
        }
        
        # Map for clean display names
        self.account_display_names = {
            "mc_cash": "MC Cash",
            "mc_bank": "MC Bank",
            "mc_mpesa": "MC Mpesa",
            "be_cash": "BE Cash",
            "be_bank": "BE Bank", 
            "be_mpesa": "BE Mpesa",
            "mcasie_cash": "MCAsie Cash",
            "cash_in_transit": "Cash In Transit",
            "royalties_available": "Royalties Available",
            "expense_provisions": "Expense Provisions",
            "fond_de_caisse": "Fond de Caisse",
            "buying_petty_cash": "Buying Petty Cash"
        }
        
        # Map to normalize account names from parsed data
        self.account_name_map = {
            # MicroConcept variations
            "mc cash": "mc_cash",
            "mc bank": "mc_bank",
            "mc mpesa": "mc_mpesa",
            "microconcept cash": "mc_cash",
            "microconcept bank": "mc_bank",
            "microconcept mpesa": "mc_mpesa",
            
            # Bellissima variations
            "be cash": "be_cash",
            "be bank": "be_bank",
            "be mpesa": "be_mpesa",
            "bellissima cash": "be_cash",
            "bellissima bank": "be_bank",
            "bellissima mpesa": "be_mpesa",
            
            # MCAsie variations
            "mcasie cash": "mcasie_cash",
            "rac": "mcasie_cash",
            "asie": "mcasie_cash",
            
            # Special accounts
            "cash in transit": "cash_in_transit",
            "royalties available": "royalties_available",
            "expense provisions": "expense_provisions",
            "fond de caisse": "fond_de_caisse",
            "buying petty cash": "buying_petty_cash"
        }
    
    def process(self, parsed_data, sender_name):
        """Process a fund transfer request"""
        # Extract data from parsed result
        try:
            amount = float(parsed_data.get("amount", 0))
            
            # Normalize account names
            from_account = self._normalize_account_name(parsed_data.get("from_account", ""))
            to_account = self._normalize_account_name(parsed_data.get("to_account", ""))
            
            # Save original names for messages
            original_from = parsed_data.get("from_account", from_account)
            original_to = parsed_data.get("to_account", to_account)
            
            purpose = parsed_data.get("purpose", "Funds Transfer")
            description = parsed_data.get("description", f"Transfer from {original_from} to {original_to} for {purpose}")
            
            # Check for MCAsie special cases as in old_brain.py
            if to_account == "mcasie_cash" and any(x in from_account for x in ["mc_", "be_"]):
                # For transfers from MC or BE to MCAsie, set to_account to Cash In Transit
                to_account = "cash_in_transit"
                logger.info(f"Converting destination to Cash In Transit for MCAsie transfer")
            elif to_account == "mcasie_cash" and not from_account:
                # If to_account is MCAsie but from_account isn't specified
                from_account = "cash_in_transit"
                logger.info(f"Setting source to Cash In Transit for MCAsie transfer with unspecified source")
            
            # Validate account IDs
            if not self.account_ids.get(from_account) or not self.account_ids.get(to_account):
                unknown_account = from_account if not self.account_ids.get(from_account) else to_account
                error_msg = f"Unknown account: {unknown_account}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
            
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
            
            # Build the API URL with organization ID
            zoho_api_url = f"{Config.ZOHO_API_URL}/banktransactions?organization_id={Config.ZOHO_ORG_ID}"
            
            # Check if this is a transfer to MCAsie (handled differently)
            is_mcasie_transfer = to_account == "mcasie_cash"
            
            # For MCAsie transfers, use a single transaction
            if is_mcasie_transfer:
                # Single transaction payload
                payload = {
                    "date": current_date,
                    "from_account_id": self.account_ids[from_account],
                    "to_account_id": self.account_ids[to_account],
                    "amount": amount,
                    "reference_number": reference_number,
                    "description": description,
                    "transaction_type": "transfer_fund"
                }
                
                # Execute the transaction
                logger.info(f"Executing direct transfer: {from_account} to {to_account}")
                response = requests.post(zoho_api_url, headers=headers, json=payload)
                
                # Check response
                if response.status_code >= 400:
                    error_msg = f"API Error ({response.status_code}): {response.text}"
                    logger.error(error_msg)
                    return {"status": "error", "text": error_msg}
                
                # Extract transaction ID
                result = response.json()
                transaction_id = result.get("banktransfer", {}).get("banktransfer_id", "Unknown")
                transaction_id_text = transaction_id
            else:
                # For all other transfers, create two transactions
                logger.info(f"Creating double transaction: {from_account} to {to_account} via Cash In Transit")
                
                # First transaction: from_account to Cash In Transit
                first_transaction = {
                    "date": current_date,
                    "from_account_id": self.account_ids[from_account],
                    "to_account_id": self.account_ids["cash_in_transit"],
                    "amount": amount,
                    "reference_number": reference_number,
                    "description": f"{description} (Part 1: {original_from} to Cash In Transit)",
                    "transaction_type": "transfer_fund"
                }
                
                # Second transaction: Cash In Transit to to_account
                second_transaction = {
                    "date": current_date,
                    "from_account_id": self.account_ids["cash_in_transit"],
                    "to_account_id": self.account_ids[to_account],
                    "amount": amount,
                    "reference_number": f"{reference_number}-2",
                    "description": f"{description} (Part 2: Cash In Transit to {original_to})",
                    "transaction_type": "transfer_fund"
                }
                
                # Execute first transaction
                first_response = requests.post(zoho_api_url, headers=headers, json=first_transaction)
                if first_response.status_code >= 400:
                    error_msg = f"API Error on first transaction ({first_response.status_code}): {first_response.text}"
                    logger.error(error_msg)
                    return {"status": "error", "text": error_msg}
                
                # Execute second transaction
                second_response = requests.post(zoho_api_url, headers=headers, json=second_transaction)
                if second_response.status_code >= 400:
                    error_msg = f"API Error on second transaction ({second_response.status_code}): {second_response.text}"
                    logger.error(error_msg)
                    return {"status": "error", "text": error_msg}
                
                # Extract transaction IDs
                first_result = first_response.json()
                second_result = second_response.json()
                first_id = first_result.get("banktransfer", {}).get("banktransfer_id", "Unknown")
                second_id = second_result.get("banktransfer", {}).get("banktransfer_id", "Unknown")
                transaction_id_text = f"{first_id} and {second_id}"
                
                # Save the full result
                result = {
                    "first_transaction": first_result,
                    "second_transaction": second_result
                }
            
            # Send success message, but don't fail if message sending fails
            if "second_transaction" in result:
                # This was a two-step transfer
                response_text = f"@{sender_name}: Successfully transferred ${amount} from {original_from} to {original_to} via Cash In Transit. Transaction ID(s): {transaction_id_text}"
            else:
                response_text = f"@{sender_name}: Successfully transferred ${amount} from {original_from} to {original_to}. Transaction ID: {transaction_id_text}"
                
            # Send the success message to Nicole channel - using same channel as old_brain.py
            logger.info(response_text)
            
            # For MCAsie transfers, also send a notification to recipient like in old_brain.py
            to_mcasie = any(key == to_account and 'mcasie' in key.lower() for key in self.account_ids.keys())
            is_cash_in_transit = to_account == 'cash_in_transit'
            if to_mcasie or is_cash_in_transit:
                recipient_msg = f"RAC: {sender_name} sent ${amount} from {original_from} to {original_to}. Please confirm receipt."
                logger.info(recipient_msg)  # old_brain.py also sent to "Nicole" channel
            
            # Return successful result with transaction info - matching old_brain.py format
            return {
                "status": "success", 
                "text": response_text,  # change from "message" to "text" to match old_brain.py
                "amount": amount, 
                "from_account": original_from, 
                "to_account": original_to
            }
            
        except Exception as e:
            error_msg = f"Error processing fund transfer: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "text": error_msg}
    
    def _normalize_account_name(self, account_name):
        """Normalize account names to match internal keys"""
        if not account_name:
            return ""
            
        # Convert to lowercase for matching
        account_name = account_name.lower()
        
        # Try direct mapping first
        normalized = self.account_name_map.get(account_name)
        if normalized:
            return normalized
            
        # Try partial matching for more flexible recognition
        for key, value in self.account_name_map.items():
            if key in account_name:
                return value
                
        # Return original if no match found
        return account_name 