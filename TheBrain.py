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
        # Try using a different URL format
        self.api_url = "https://x.ai/api/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("X.ai API key not found in environment variables")
        
        # Configure SSL settings for Heroku environment
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Create a standard requests session without custom SSL config
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
                "x-api-key": self.api_key,  # X.ai requires x-api-key header
                "Content-Type": "application/json"
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
            - Valid account names are: cash_in_transit, be_bank, bellissima, mcasie, bdms
            - If an account name is not specified, use a reasonable default
            - Amount should be a number, remove any currency symbols or commas
            """
            
            # Create the request payload according to X.ai documentation
            payload = {
                "model": "grok-2",  # Updated to use grok-2 as per X.ai docs
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.1,
                "max_tokens": 150
            }
            
            try:
                # Try using the session first
                response = self.session.post(
                    self.api_url, 
                    headers=headers, 
                    json=payload,
                    timeout=30  # Standard timeout
                )
            except (requests.exceptions.SSLError, requests.exceptions.ConnectionError) as e:
                # If session fails with SSL or connection error, try a direct request
                logger.warning(f"Session request failed with {type(e).__name__}: {str(e)}. Trying direct request.")
                
                # Try a different API URL format
                api_url = "https://api.x.ai/v1/chat/completions"  # Alternative URL format
                
                # Add Authorization header as backup
                headers["Authorization"] = f"Bearer {self.api_key}"
                
                # Make a direct request without session
                response = requests.request(
                    "POST",
                    api_url,
                    headers=headers,
                    json=payload,
                    timeout=30
                )
            
            # Log response status and headers for debugging
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            if "choices" not in result or not result["choices"]:
                raise Exception("No response from X.ai API")
            
            # Extract the parsed data
            parsed_data = result["choices"][0]["message"]["content"]
            
            # Parse the JSON string into a dictionary
            try:
                parsed_data = json.loads(parsed_data)
            except json.JSONDecodeError as e:
                logger.error(f"Failed to parse JSON response: {e}")
                raise Exception("Invalid response format from X.ai API")
            
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
    
    def handle_message(self, message, channel):
        """Handle incoming messages"""
        try:
            # Parse the message using X.ai API
            parsed_data = self.grok_client.parse_message(message)
            
            # Validate parsed data
            if not isinstance(parsed_data, dict):
                raise ValueError("Invalid response format from X.ai API")
                
            required_fields = ["amount", "from_account", "to_account"]
            missing_fields = [field for field in required_fields if field not in parsed_data]
            if missing_fields:
                raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
            
            # Process the parsed data
            if parsed_data:
                # Execute the fund transfer
                result = self.fund_transfer_handler.process(parsed_data)
                
                # Send success message
                success_message = f"✅ Transfer completed successfully!\nAmount: {result['amount']}\nFrom: {result['from_account']}\nTo: {result['to_account']}"
                self.message_sender.send_message(channel, success_message)
            else:
                # Send error message if parsing failed
                error_message = "❌ Sorry, I couldn't understand the transfer details. Please try again with a clearer message."
                self.message_sender.send_message(channel, error_message)
                
        except ValueError as e:
            logger.error(f"Validation error: {str(e)}")
            error_message = f"❌ Invalid request format: {str(e)}"
            self.message_sender.send_message(channel, error_message)
        except requests.exceptions.SSLError as e:
            logger.error(f"SSL Error: {str(e)}")
            error_message = "❌ Connection error while contacting X.ai API. Please try again later."
            self.message_sender.send_message(channel, error_message)
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection Error: {str(e)}")
            error_message = "❌ Unable to connect to X.ai API. Please check network connection and try again later."
            self.message_sender.send_message(channel, error_message)
        except Exception as e:
            logger.error(f"Error processing message: {str(e)}")
            error_message = f"❌ An error occurred: {str(e)}"
            self.message_sender.send_message(channel, error_message)

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
        
        if not message:
            return jsonify({"error": "No message found in request"}), 400
            
        # Process the message using TheBrain
        brain.handle_message(message, channel)
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