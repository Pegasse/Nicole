from flask import Flask, request, jsonify
import requests
import certifi
import ssl
import urllib3
import socket
from utils.message_sender import CliqMessageSender
from operations.fund_transfer import FundTransferHandler
from config import Config, logger
from utils.token_manager import ZohoTokenManager
import json

# Create Flask application
app = Flask(__name__)

class GrokAPIClient:
    """Client for interacting with the X.ai API"""
    
    def __init__(self):
        """Initialize the X.ai API client"""
        self.api_key = Config.GROK_API_KEY
        
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

class Brain:
    """Main brain class that coordinates message processing and business logic"""
    
    def __init__(self):
        """Initialize the brain with necessary components"""
        self.token_manager = ZohoTokenManager()
        self.message_sender = CliqMessageSender()
        self.fund_transfer_handler = FundTransferHandler(self.token_manager)
        self.grok_client = GrokAPIClient()
    
    def handle_message(self, message, channel, sender_name="system"):
        """Handle incoming messages
        
        Args:
            message (str): The message to process
            channel (str): The channel to send responses to
            sender_name (str): The name of the message sender, defaults to "system"
        """
        try:
            # Parse the message using X.ai API
            parsed_data = self.grok_client.parse_message(message)
            
            # Check if we have an error in parsed data
            if "error" in parsed_data:
                # If this is a parse error, extract the original response to provide feedback
                original_response = parsed_data.get("original_response", "")
                if original_response and len(original_response) > 50:
                    original_response = original_response[:50] + "..."
                    
                error_message = f"❌ I had trouble understanding your request. The AI responded with: {original_response}\n\nPlease try again with a clearer message, for example: 'Transfer $500 from BE bank to cash in transit'"
                self.message_sender.send_message(channel, error_message)
                return
                
            # Validate parsed data
            if not isinstance(parsed_data, dict):
                raise ValueError("Invalid response format from X.ai API")
                
            required_fields = ["amount", "from_account", "to_account"]
            missing_fields = [field for field in required_fields if field not in parsed_data]
            if missing_fields:
                error_message = f"❌ I couldn't extract all the required information from your message. Missing: {', '.join(missing_fields)}.\n\nPlease try again with a clearer message including amount, source account, and destination account."
                self.message_sender.send_message(channel, error_message)
                return
            
            # Additional validation - amount should be a number
            try:
                amount = float(parsed_data["amount"])
                if amount <= 0:
                    raise ValueError("Amount must be positive")
                # Update the parsed data with the converted amount
                parsed_data["amount"] = amount
            except (ValueError, TypeError):
                error_message = f"❌ The amount '{parsed_data['amount']}' doesn't seem to be a valid number. Please specify a positive number."
                self.message_sender.send_message(channel, error_message)
                return
            
            # Process the parsed data
            result = self.fund_transfer_handler.process(parsed_data, sender_name)
            
            # If result contains a status and message, we can use those
            if result and isinstance(result, dict) and "status" in result:
                if result["status"] == "success":
                    # Send success message
                    success_message = f"✅ Transfer completed successfully!\nAmount: {result.get('amount')}\nFrom: {result.get('from_account')}\nTo: {result.get('to_account')}"
                    self.message_sender.send_message(channel, success_message)
                else:
                    # Send the error message from the result
                    error_message = f"❌ Transfer failed: {result.get('message', 'Unknown error')}"
                    self.message_sender.send_message(channel, error_message)
            else:
                # Fallback success message if result format is unexpected
                logger.warning(f"Unexpected result format from fund_transfer_handler: {result}")
                self.message_sender.send_message(channel, "✅ Transfer request processed.")
            
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            error_message = f"❌ Invalid request format: {str(e)}"
            try:
                self.message_sender.send_message(channel, error_message)
            except Exception as msg_error:
                logger.error(f"Failed to send error message: {str(msg_error)}")
        except requests.exceptions.SSLError as e:
            logger.error(f"SSL Error: {str(e)}")
            error_message = "❌ Connection error while contacting X.ai API. Please try again later."
            try:
                self.message_sender.send_message(channel, error_message)
            except Exception as msg_error:
                logger.error(f"Failed to send error message: {str(msg_error)}")
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection Error: {str(e)}")
            error_message = "❌ Unable to connect to X.ai API. Please check network connection and try again later."
            try:
                self.message_sender.send_message(channel, error_message)
            except Exception as msg_error:
                logger.error(f"Failed to send error message: {str(msg_error)}")
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}", exc_info=True)
            error_message = f"❌ An error occurred: {str(e)}"
            try:
                self.message_sender.send_message(channel, error_message)
            except Exception as msg_error:
                logger.error(f"Failed to send error message: {str(msg_error)}")

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
        channel = data.get("channel", "Nicole")  # Default to "Nicole" if channel not specified
        sender_name = data.get("sender_name", "system")  # Extract sender name or use default
        
        if not message:
            return jsonify({"error": "No message found in request"}), 400
            
        # Process the message using TheBrain, passing sender_name
        brain.handle_message(message, channel, sender_name)
        return jsonify({"status": "success"})
        
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({"error": str(e)}), 500

def start_server():
    """Start the Flask server"""
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=False
    )

if __name__ == '__main__':
    start_server() 