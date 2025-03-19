from flask import Flask, request, jsonify
import requests
import certifi
import ssl
import urllib3
import socket
from operations.fund_transfer import FundTransferHandler
from operations.expense import ExpenseHandler
from config import Config, logger
from utils.token_manager import ZohoTokenManager
import json
import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Add the current directory to the path to import local modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

# Create Flask application
app = Flask(__name__)
app.secret_key = Config.FLASK_SECRET_KEY

class GrokAPIClient:
    """Client for interacting with the X.ai API"""
    
    def __init__(self):
        """Initialize the X.ai API client"""
        self.api_key = Config.X_AI_API_KEY
        
        # Use the official API endpoint
        self.api_url = "https://api.x.ai/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("X.ai API key not found in environment variables")
        
        # Create a standard requests session
        self.session = requests.Session()
        
        # Simple retry configuration
        retry_strategy = urllib3.Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["POST"]
        )
        
        # Use a standard adapter
        adapter = requests.adapters.HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
    
    def parse_message(self, message):
        """Parse a message using the X.ai API"""
        if not self.api_key:
            raise Exception("X.ai API key not configured")
        
        try:
            # Prepare the API request according to X.ai documentation
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "NicoleBot/1.0"
            }
            
            # Create the system prompt
            system_content = """You are a helpful assistant that parses natural language messages about fund transfers.
            Extract the following information from the message:
            - amount: The amount to transfer (as a number)
            - from_account: The source account name
            - to_account: The destination account name
            
            Return the information in JSON format:
            {
                "amount": number,
                "from_account": string,
                "to_account": string
            }
            
            Special rules:
            - Account names should be lowercase and use underscores for spaces
            - Valid account names and their variations:
              * MC Cash (variations: mc_cash, microconcept cash, mc cash account)
              * MC Bank (variations: mc_bank, microconcept bank, mc bank account)
              * MC Mpesa (variations: mc_mpesa, microconcept mpesa, mc mpesa account)
              * BE Cash (variations: be_cash, bellissima cash, bellissima cash account, belli cash)
              * BE Bank (variations: be_bank, bellissima bank, bellissima bank account, belli bank)
              * BE Mpesa (variations: be_mpesa, bellissima mpesa, bellissima mpesa account, belli mpesa)
              * MCAsie Cash (variations: mcasie_cash, mcasie, rac, asie, mcasie cash account)
              * Cash In Transit (variations: cash_in_transit, transit, cash transit)
              * Royalties Available (variations: royalties_available, royalties, available royalties)
              * Expense Provisions (variations: expense_provisions, provisions, expense provision)
              * Fond de Caisse (variations: fond_de_caisse, fond, caisse)
              * Buying Petty Cash (variations: buying_petty_cash, petty cash, buying petty)
            
            Account name matching rules:
            - For MCAsie/RAC transfers:
              * If destination is MCAsie/RAC and source is MC or BE account, set to_account to 'cash_in_transit'
              * If destination is MCAsie/RAC but source isn't specified, set from_account to 'cash_in_transit'
            - For withdrawals:
              * If no to_account is specified, set it to a Cash account with similar prefix to from_account
              * Example: BE Bank to BE Cash
            
            - If an account name is not specified, use a reasonable default
            - Amount should be a number, remove any currency symbols or commas
            """
            
            # Create the request payload according to X.ai documentation
            payload = {
                "model": "grok-2",
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.1,
                "max_tokens": 150
            }
            
            # Make the API request
            response = self.session.post(
                self.api_url, 
                headers=headers, 
                json=payload,
                timeout=30
            )
            
            # Log response status and headers for debugging
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            
            # Log raw response body for debugging
            try:
                logger.debug(f"Raw response: {response.text}")
            except:
                logger.debug("Could not log raw response text")
            
            response.raise_for_status()
            
            # Parse the response
            try:
                result = response.json()
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse API response as JSON: {e}")
                logger.error(f"Raw response: {response.text}")
                raise Exception(f"Invalid JSON response from X.ai API: {response.text[:100]}")
            
            # Check if response has expected structure
            if "choices" not in result:
                logger.error(f"Unexpected API response format - missing 'choices': {result}")
                raise Exception("Unexpected response format from X.ai API - missing 'choices'")
                
            if not result["choices"]:
                logger.error(f"API returned empty choices array: {result}")
                raise Exception("No response choices from X.ai API")
            
            # Get the first choice
            first_choice = result["choices"][0]
            if "message" not in first_choice:
                logger.error(f"Missing 'message' in response choice: {first_choice}")
                raise Exception("Unexpected response format from X.ai API - missing 'message'")
                
            if "content" not in first_choice["message"]:
                logger.error(f"Missing 'content' in response message: {first_choice['message']}")
                raise Exception("Unexpected response format from X.ai API - missing 'content'")
            
            # Extract the parsed data text
            parsed_data_text = first_choice["message"]["content"]
            if not parsed_data_text or not parsed_data_text.strip():
                logger.error("Empty content received from X.ai API")
                raise Exception("Empty response content from X.ai API")
            
            # Try to extract JSON from the response content
            # First look for JSON within the content (in case there's additional text)
            json_start = parsed_data_text.find("{")
            json_end = parsed_data_text.rfind("}")
            
            if json_start != -1 and json_end != -1 and json_end > json_start:
                # Extract just the JSON part
                json_str = parsed_data_text[json_start:json_end+1]
                try:
                    parsed_data = json.loads(json_str)
                    logger.info(f"Successfully extracted JSON from response content")
                except json.JSONDecodeError as e:
                    logger.error(f"Found JSON-like content but failed to parse: {e}")
                    logger.error(f"JSON string: {json_str}")
                    # Fall back to trying the entire content
                    try:
                        parsed_data = json.loads(parsed_data_text)
                    except json.JSONDecodeError as e2:
                        logger.error(f"Failed to parse entire content as JSON: {e2}")
                        # Use a default response with placeholder values
                        logger.info("Using default response structure")
                        parsed_data = {
                            "amount": 0,
                            "from_account": "unknown",
                            "to_account": "unknown",
                            "error": "Failed to parse response",
                            "original_response": parsed_data_text
                        }
            else:
                # If no JSON brackets found, try the whole string
                try:
                    parsed_data = json.loads(parsed_data_text)
                except json.JSONDecodeError as e:
                    logger.error(f"Failed to parse response as JSON: {e}")
                    logger.error(f"Response content: {parsed_data_text}")
                    # Use a default response with placeholder values
                    parsed_data = {
                        "amount": 0,
                        "from_account": "unknown",
                        "to_account": "unknown",
                        "error": "Failed to parse response",
                        "original_response": parsed_data_text
                    }
            
            # Log the parsed data
            logger.info(f"Parsed message: {message}")
            logger.info(f"Parsed data: {parsed_data}")
            
            return parsed_data
            
        except requests.exceptions.SSLError as e:
            logger.error(f"SSL Error: {str(e)}")
            logger.error("SSL Certificate verification failed. Please check the API endpoint and SSL configuration.")
            raise
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection Error: {str(e)}")
            logger.error("Failed to connect to the API. Please check your internet connection and the API endpoint.")
            raise
        except requests.exceptions.Timeout as e:
            logger.error(f"Request Timeout: {str(e)}")
            raise
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to X.ai API: {str(e)}")
            if hasattr(e, 'response'):
                logger.error(f"Response status: {e.response.status_code}")
                logger.error(f"Response headers: {e.response.headers}")
                try:
                    logger.error(f"Response body: {e.response.json()}")
                except:
                    logger.error(f"Response body: {e.response.text}")
            raise
        except Exception as e:
            logger.error(f"Error parsing message: {str(e)}")
            raise

    def parse_message_with_system_content(self, message, system_content):
        """Parse a message using the X.ai API with custom system content."""
        if not self.api_key:
            raise Exception("X.ai API key not configured")
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "NicoleBot/1.0"
            }
    
            payload = {
                "model": "grok-2",
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.1,
                "max_tokens": 150
            }
            
            response = self.session.post(self.api_url, headers=headers, json=payload, timeout=30)
            response.raise_for_status()
            result = response.json()
            parsed_data_text = result["choices"][0]["message"]["content"]
            
            # Extract JSON from the response
            json_start = parsed_data_text.find("{")
            json_end = parsed_data_text.rfind("}")
            
            if json_start != -1 and json_end != -1 and json_end > json_start:
                json_str = parsed_data_text[json_start:json_end+1]
                try:
                    parsed_data = json.loads(json_str)
                except json.JSONDecodeError:
                    parsed_data = json.loads(parsed_data_text)
            else:
                parsed_data = json.loads(parsed_data_text)
                
            return parsed_data
            
        except Exception as e:
            logger.error(f"Error parsing message: {str(e)}")
            raise

    def classify_transaction_type(self, message):
        """Classify the transaction type as fund_transfer, expense, or unknown."""
        system_content = """You are a financial transaction classifier for a Zoho Books accounting system that categorizes messages.

Classify the message as one of:
1. 'fund_transfer' - For moving money between asset accounts (bank accounts, cash accounts, etc.)
2. 'expense' - For recording expenses paid from an asset account to an expense account
3. 'unknown' - If the message doesn't clearly indicate a financial transaction

Examples for fund_transfer:
- "Transfer 5000 from MC bank to BE cash"
- "Move 1000 from BE Bank to MC Cash"
- "Send 800 from MC Cash to MCAsie"
- "Withdraw 200 from BE Bank to BE Cash"
- "Transfer 1500 from Royalties to MC Bank"

Examples for expense:
- "Record 200 for office supplies paid from petty cash"
- "Expense 300 for marketing paid through BE Bank"
- "Pay 150 for internet bill from MC Bank"
- "Record expense of 450 for transport paid through BE Mpesa"
- "Spend 250 on stationery paid from Buying Petty Cash"
- "I bought 20 brooms worth 30$ each"
- "Purchased office furniture for 500$"
- "Bought inventory items for 1000$"
- "Spent 75$ on cleaning supplies"

IMPORTANT RULES:
1. Any message mentioning "bought", "purchased", "paid for", or "spent on" should be classified as 'expense'
2. Amounts with quantity (e.g., "20 brooms at $30 each") are almost always expenses
3. When in doubt between 'expense' and 'unknown', classify as 'expense'

Return ONLY this JSON format:
{
  "transaction_type": "fund_transfer" or "expense" or "unknown"
}
"""
        parsed_data = self.parse_message_with_system_content(message, system_content)
        return parsed_data["transaction_type"]

class Brain:
    """Main brain class that coordinates message processing and business logic"""
    
    def __init__(self):
        """Initialize the brain with necessary components"""
        self.token_manager = token_manager
        self.grok_client = GrokAPIClient()
        self.fund_transfer_handler = FundTransferHandler(self.token_manager)
        self.expense_handler = ExpenseHandler(self.token_manager)
    
    def handle_message(self, message, channel, sender_name="system"):
        """Handle incoming messages and process transactions."""
        try:
            # Step 1: Classify the transaction type
            transaction_type = self.grok_client.classify_transaction_type(message)

            # Step 2: Fetch accounts from Zoho Books
            try:
                cash_bank_accounts = self.token_manager.get_asset_accounts()
                logger.info(f"Fetched {len(cash_bank_accounts)} cash and bank accounts from Zoho Books")
                # Create a formatted list for the prompts
                cash_bank_account_list = "\n".join([
                    f"- {acc['account_name']}, ID: {acc['account_id']} ({acc.get('account_type', 'account')})" 
                    for acc in cash_bank_accounts
                ])
            except Exception as e:
                logger.warning(f"Failed to fetch cash and bank accounts: {str(e)}")
                cash_bank_account_list = "Unable to fetch cash and bank accounts from Zoho Books. Please specify account names clearly."
                cash_bank_accounts = []

            if transaction_type == "fund_transfer":
                # Step 3: Load fund transfer instructions
                with open("instructions/Internal Fund Transfer.txt", "r") as f:
                    instructions = f.read()
                
                # Step 5: Define system content with Zoho accounts
                system_content = f"""{instructions}

Available cash and bank accounts for transfers:
{cash_bank_account_list}

Extract the following information from the message in JSON format:
{{
    "amount": number (positive value without currency symbols),
    "from_account": string (source account name - use common names like "BE Cash", "MC Bank", etc.),
    "to_account": string (destination account name - use common names like "BE Cash", "MC Bank", etc.),
    "reference": string (optional brief reason for transfer)
}}

Common account names you can use:
- MC Cash - Microconcept's cash account
- MC Bank - Microconcept's bank account 
- BE Cash - Bellissima's cash account
- BE Bank - Bellissima's bank account
- MCAsie Cash - The purchasing office cash account
- Cash In Transit - Used for transfers to MCAsie
- Expense Provisions - Main cash account for expenses

Return ONLY valid JSON format. Do not add any explanations or extra text.
"""
                parsed_data = self.grok_client.parse_message_with_system_content(message, system_content)
                # Step 6: Process fund transfer
                result = self.fund_transfer_handler.process(parsed_data, sender_name)

            elif transaction_type == "expense":
                # Step 7: Fetch expense accounts
                try:
                    expense_accounts = self.token_manager.get_expense_accounts()
                    expense_account_list = "\n".join([
                        f"- {acc['account_name']}, ID: {acc['account_id']}" 
                        for acc in expense_accounts
                    ])
                except Exception as e:
                    logger.warning(f"Failed to fetch expense accounts: {str(e)}")
                    expense_account_list = "Unable to fetch expense accounts. Please specify the expense account name clearly."
                
                # Step 8: Load expense instructions
                with open("instructions/Expenses.txt", "r") as f:
                    instructions = f.read()
                
                # Step 9: Create system content with fetched accounts
                system_content = f"""{instructions}

Here are the available expense accounts:
{expense_account_list}

Here are the available payment accounts (cash & bank):
{cash_bank_account_list}

Parse the message and extract the following information in JSON format:
{{
    "amount": number (positive value without currency symbols),
    "account_id": string (optional ID from expense accounts list - only include if specified),
    "account_name": string (name of the expense account - use the best match from above),
    "paid_through": string (payment account name - use common names like "BE Cash", "MC Bank", etc.),
    "date": string (YYYY-MM-DD format, default to today if unspecified),
    "reference": string (brief description, max 10 words),
    "notes": string (detailed description if provided),
    "currency": string (currency code or symbol if mentioned, e.g., "USD", "EUR", "$", "€")
}}

IMPORTANT: 
- Common payment account names include: "Expense Provisions", "MC Cash", "BE Cash", "Buying Petty Cash"
- For expenses related to a specific company (MC, BE, etc.), use the corresponding cash account
- If no payment account is specified, use "Expense Provisions"
- Extract any currency information (USD, EUR, €, $, etc.) from the message. Default to USD if not specified.
- Include the original amount with any currency symbols in the notes.

Example JSON responses:
For "I bought 20 brooms worth $30 each":
{{
  "amount": 600,
  "account_name": "Office Supplies",
  "paid_through": "Expense Provisions",
  "date": "2025-03-18",
  "reference": "Office supplies purchase",
  "notes": "Purchased 20 brooms at $30 each for office cleaning",
  "currency": "USD"
}}

For "Paid 500 EUR for office rent":
{{
  "amount": 500,
  "account_name": "Rent",
  "paid_through": "MC Bank",
  "date": "2025-03-18",
  "reference": "Monthly office rent",
  "notes": "Payment for office rent in euros",
  "currency": "EUR"
}}

Return ONLY valid JSON with no additional text.
"""
                
                parsed_data = self.grok_client.parse_message_with_system_content(message, system_content)
                # Step 10: Process expense
                result = self.expense_handler.process(parsed_data, sender_name)

            else:
                return "I couldn't determine the type of transaction. Please specify if it's a fund transfer or an expense."

            # Step 11: Handle the result
            if result and isinstance(result, dict) and "status" in result:
                if result["status"] == "success":
                    return result["text"]
                else:
                    return f"❌ Transaction failed: {result.get('text', 'Unknown error')}"
            else:
                logger.warning(f"Unexpected result format: {result}")
                return "✅ Transaction request processed."
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}", exc_info=True)
            return f"❌ An error occurred: {str(e)}"

# Initialize components
token_manager = ZohoTokenManager()
brain = Brain()

@app.route('/auth')
def auth():
    """Initialize OAuth flow"""
    return token_manager.initialize_oauth_flow()

@app.route('/auth/callback')
def auth_callback():
    """Handle OAuth callback"""
    code = request.args.get('code')
    if not code:
        return "Error: No authorization code received", 400
    return token_manager.handle_oauth_callback(code)

@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming webhook requests"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400
            
        # Extract message and channel from the data
        message = data.get("message")
        channel = data.get("channel", "Nicole")
        sender_name = data.get("sender_name", "system")
        
        if not message:
            return jsonify({"error": "No message found in request"}), 400
            
        # Process the message and get the response
        response_text = brain.handle_message(message, channel, sender_name)
        return jsonify({"text": response_text})
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({"text": f"❌ An error occurred: {str(e)}"}), 500

def start_server():
    """Start the Flask server"""
    app.run(
        host="0.0.0.0",
        port=Config.PORT,
        debug=False
    )

if __name__ == '__main__':
    start_server() 