import os
import json
from flask import Flask, request, redirect, jsonify
from datetime import datetime
import logging
from dotenv import load_dotenv

# Import operation handlers
from operations.fund_transfer import FundTransferHandler
from utils.token_manager import ZohoTokenManager
from utils.api_client import GrokAPIClient
from utils.message_sender import CliqMessageSender
from config import Config, logger
from brain import Brain

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key-here')

# Print startup information
logger.info("====== App starting up ======")
logger.info(f"Current working directory: {os.getcwd()}")

# Initialize components
token_manager = ZohoTokenManager()
grok_client = GrokAPIClient()
cliq_sender = CliqMessageSender()
brain = Brain(token_manager)

# Initialize operation handlers
fund_transfer_handler = FundTransferHandler(token_manager)

@app.route("/auth")
def auth():
    """Initiate the OAuth flow"""
    return token_manager.initialize_oauth_flow()

@app.route("/auth/callback")
def auth_callback():
    """Handle the OAuth callback from Zoho"""
    code = request.args.get("code")
    if not code:
        return "Error: No authorization code received", 400
    
    return token_manager.handle_oauth_callback(code)

def get_app_url():
    """Get the application URL from config"""
    return Config.APP_URL

def determine_operation_type(parsed_data):
    """Determine which operation handler to use based on the parsed data"""
    # Currently we only have fund transfers
    # In the future, we'll add logic to determine other operation types
    return "fund_transfer"

@app.route("/webhook", methods=["POST"])
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

if __name__ == "__main__":
    # Get the port from environment variable or use default
    port = int(os.environ.get("PORT", 8080))
    
    # Check if we need to set up OAuth
    if not os.environ.get("ZOHO_REFRESH_TOKEN"):
        logger.info("No valid refresh token found. Please visit /auth endpoint to set up OAuth.")
    
    # Start the webhook server
    logger.info(f"Starting webhook server on port {port}...")
    start_server() 