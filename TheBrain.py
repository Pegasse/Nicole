from flask import Flask, request, jsonify
from utils.api_client import GrokAPIClient
from utils.message_sender import CliqMessageSender
from operations.fund_transfer import FundTransferHandler
from config import Config, logger
from utils.token_manager import ZohoTokenManager

# Create Flask application
app = Flask(__name__)

class Brain:
    """Main coordinator for message processing and business logic"""
    
    def __init__(self, token_manager):
        """Initialize Brain with necessary components"""
        self.token_manager = token_manager
        self.grok_client = GrokAPIClient()
        self.cliq_sender = CliqMessageSender()
        self.fund_transfer_handler = FundTransferHandler(token_manager)
    
    def determine_operation_type(self, parsed_data):
        """Determine the type of operation based on parsed data"""
        # Currently only supporting fund transfers
        # Can be extended to support more operations
        return "fund_transfer"
    
    def handle_message(self, data):
        """Process incoming messages and route to appropriate handlers"""
        try:
            # Extract message and sender
            message = data.get("message")
            sender_id = data.get("sender_id")
            sender_name = data.get("sender_name", sender_id)
            
            if not message:
                logger.warning("No message found in request data")
                return {"status": "error", "text": "No message found in request"}
            
            if not sender_id and not sender_name:
                logger.warning("No sender information found in request data")
                sender_name = "Unknown User"
            
            # Parse the message using Grok API
            parsed_data = self.grok_client.parse_message(message)
            logger.info(f"Parsed data: {parsed_data}")
            
            # Check if we have minimum required information
            if not parsed_data.get("amount"):
                response_text = f"@{sender_name}: I couldn't understand your request. Please include an amount to transfer."
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "text": response_text}
            
            # Determine operation type
            operation_type = self.determine_operation_type(parsed_data)
            
            # Route to appropriate handler
            if operation_type == "fund_transfer":
                result = self.fund_transfer_handler.process(parsed_data, sender_name)
                return result
            else:
                response_text = f"@{sender_name}: Unsupported operation type."
                self.cliq_sender.send_message("Nicole", response_text)
                return {"status": "error", "text": response_text}
                
        except Exception as e:
            error_message = f"Error processing message: {str(e)}"
            logger.error(error_message, exc_info=True)
            return {"status": "error", "text": error_message}

# Initialize components
token_manager = ZohoTokenManager()
brain = Brain(token_manager)

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
            
        # Process the message using TheBrain
        response = brain.handle_message(data)
        return jsonify(response)
        
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