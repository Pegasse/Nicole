import requests
import json
from flask import Flask, request, redirect, url_for
from datetime import date, datetime, timedelta
import os
import webbrowser
import threading
import time

# ====== IMPORTANT: ZOHO API CREDENTIALS SETUP ======
# If you encounter "invalid_client" or "invalid_code" errors:
# 1. Go to https://api-console.zoho.com/
# 2. Select your application or create a new one
# 3. Generate a self-client token by clicking "Generate Code" 
# 4. For the scope, use "ZohoBooks.fullaccess.all"
# 5. Update the ZOHO_CLIENT_ID, ZOHO_CLIENT_SECRET, and ZOHO_REFRESH_TOKEN below
# ===================================================

app = Flask(__name__)

# Add debugging information at startup
print("====== TheBrain.py - Starting up ======")
print(f"Current working directory: {os.getcwd()}")

# Grok API setup
GROK_API_URL = "https://api.x.ai/v1/chat/completions"  # Grok API URL
GROK_API_KEY = "xai-x6xw570Xz2Bxd9uBiNf9dhd5hntUexpKimXWc85a8QYbcBLMaaUWDXCNxfFLsXWtqDtvml32YkXKuJRw"  # Your Grok API key
GROK_HEADERS = {
    "Authorization": f"Bearer {GROK_API_KEY}",
    "Content-Type": "application/json",
}

# Zoho Books API setup
ZOHO_API_URL = "https://www.zohoapis.com/books/v3"
ZOHO_ORG_ID = "880025675"  # Your Zoho Org ID
print(f"Zoho organization ID: {ZOHO_ORG_ID}")

# Zoho OAuth configuration
# These credentials should be updated if you get an "invalid_client" error
# Generate new credentials at https://api-console.zoho.com/
ZOHO_CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID", "1000.5U3WUTZJPNVRB6FPNB4LMXYJN9N4GC")
ZOHO_CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET", "eb9b1d5dbc5abbd22e9e2a7da48c02ad61fa99a2d9")
ZOHO_SCOPE = "ZohoBooks.fullaccess.all"
ZOHO_REDIRECT_URI = "https://0add-185-203-122-107.ngrok-free.app/callback"

# Add your refresh token here - this is required for token refresh to work
# This refresh token needs to be generated for the same client ID above
ZOHO_REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN", "1000.91c418adad92c23f178df1da76a7bac5.ca2a13216dcc884b3dd0b2b9359f1ed5")

# Report on credential status
print(f"Zoho Credentials Status:")
print(f"- Client ID: {'✓ Present' if ZOHO_CLIENT_ID else '✗ Missing'}")
print(f"- Client Secret: {'✓ Present' if ZOHO_CLIENT_SECRET else '✗ Missing'}")
print(f"- Refresh Token: {'✓ Present' if ZOHO_REFRESH_TOKEN else '✗ Missing'}")
print(f"- Client ID Length: {len(ZOHO_CLIENT_ID)}")
print(f"- Client Secret Length: {len(ZOHO_CLIENT_SECRET)}") # Should typically be 64 characters

# Current token and expiry
ZOHO_TOKEN = None  # Initialize as None instead of using refresh token
print("Initial access token: None (will be refreshed on first use)")
ZOHO_TOKEN_EXPIRY = datetime.now() - timedelta(minutes=5)  # Set to expired so it forces a refresh on first use

ZOHO_HEADERS = {
    "Content-Type": "application/json",
}

# Account IDs for the transfer
MC_CASH_ID = "6122712000000091463"  # MC Cash account ID
CASH_IN_TRANSIT_ID = "6122712000000091501"  # Cash in Transit account ID
MCASIE_CASH_ID = "6122712000000091505"  # MCAsie Cash account ID (for future confirmation logic)

# Cliq webhook port
CLIQ_WEBHOOK_PORT = 5000

# Global variable to store the authorization code
auth_code = None

@app.route("/callback")
def callback():
    """Handle the OAuth callback from Zoho"""
    global auth_code
    auth_code = request.args.get("code")
    if not auth_code:
        return "Error: No authorization code received", 400
    
    return """
    <h1>Authorization Code Received!</h1>
    <p>You can now close this window and return to the terminal.</p>
    <script>
        window.close();
    </script>
    """

def get_initial_code():
    """Get the initial authorization code from Zoho"""
    global auth_code
    auth_code = None
    
    # Start Flask server in a separate thread
    def run_flask():
        app.run(port=CLIQ_WEBHOOK_PORT, use_reloader=False)
    
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Generate the authorization URL
    auth_url = "https://accounts.zoho.com/oauth/v2/auth"
    params = {
        "response_type": "code",
        "client_id": ZOHO_CLIENT_ID,
        "scope": ZOHO_SCOPE,
        "redirect_uri": ZOHO_REDIRECT_URI,
        "access_type": "offline",
        "prompt": "consent"
    }
    auth_url = f"{auth_url}?{'&'.join(f'{k}={v}' for k,v in params.items())}"
    
    print("\nOpening browser for Zoho authorization...")
    webbrowser.open(auth_url)
    
    print("\nWaiting for authorization code...")
    while auth_code is None:
        time.sleep(1)
    
    return auth_code

def get_refresh_token(code):
    """Exchange authorization code for refresh token"""
    token_url = "https://accounts.zoho.com/oauth/v2/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": ZOHO_CLIENT_ID,
        "client_secret": ZOHO_CLIENT_SECRET,
        "code": code,
        "redirect_uri": ZOHO_REDIRECT_URI
    }
    
    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status()
        result = response.json()
        
        if "refresh_token" in result:
            print("\nSuccess! Here are your tokens:")
            print(f"Refresh Token: {result['refresh_token']}")
            print(f"Access Token: {result['access_token']}")
            print(f"Expires in: {result.get('expires_in', 'unknown')} seconds")
            
            # Update the global tokens
            global ZOHO_REFRESH_TOKEN, ZOHO_TOKEN, ZOHO_TOKEN_EXPIRY, ZOHO_HEADERS
            ZOHO_REFRESH_TOKEN = result['refresh_token']
            ZOHO_TOKEN = result['access_token']
            expires_in = result.get('expires_in', 3600)
            ZOHO_TOKEN_EXPIRY = datetime.now() + timedelta(seconds=expires_in - 300)
            ZOHO_HEADERS["Authorization"] = f"Zoho-oauthtoken {ZOHO_TOKEN}"
            
            return result
        else:
            print(f"Error: No refresh token in response: {result}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        if hasattr(e.response, 'text'):
            print(f"Response: {e.response.text}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {e}")
        print(f"Raw response: {response.text}")
        return None

def setup_zoho_auth():
    """Main function to handle the OAuth setup process"""
    print("\n=== Zoho OAuth Setup ===")
    print("This will help you get a new refresh token for Zoho Books API.")
    
    # Get the initial authorization code
    code = get_initial_code()
    if not code:
        print("Failed to get authorization code.")
        return False
    
    # Exchange the code for tokens
    result = get_refresh_token(code)
    if result:
        print("\nTokens have been automatically updated in the code.")
        print("You can now use the application.")
        return True
    else:
        print("\nFailed to get refresh token. Please try again.")
        return False

# Function to refresh the Zoho token
def refresh_zoho_token():
    global ZOHO_TOKEN, ZOHO_TOKEN_EXPIRY, ZOHO_HEADERS
    
    if not ZOHO_CLIENT_ID or not ZOHO_CLIENT_SECRET or not ZOHO_REFRESH_TOKEN:
        print(f"Error: Missing Zoho OAuth credentials. Client ID: {'✓' if ZOHO_CLIENT_ID else '✗'}, Client Secret: {'✓' if ZOHO_CLIENT_SECRET else '✗'}, Refresh Token: {'✓' if ZOHO_REFRESH_TOKEN else '✗'}")
        return False
    
    try:
        print(f"Attempting to refresh token with refresh token: {ZOHO_REFRESH_TOKEN[:10]}...")
        refresh_url = "https://accounts.zoho.com/oauth/v2/token"
        payload = {
            "client_id": ZOHO_CLIENT_ID,
            "client_secret": ZOHO_CLIENT_SECRET,
            "refresh_token": ZOHO_REFRESH_TOKEN,
            "grant_type": "refresh_token"
        }
        
        # Print debug info for the request
        print(f"Token refresh request details:")
        print(f"- URL: {refresh_url}")
        print(f"- Client ID: {ZOHO_CLIENT_ID[:8]}...")
        print(f"- Client Secret: {ZOHO_CLIENT_SECRET[:8]}...")
        print(f"- Refresh Token: {ZOHO_REFRESH_TOKEN[:8]}...")
        
        response = requests.post(refresh_url, data=payload)
        print(f"Refresh token response: {response.status_code}")
        print(f"Response body: {response.text}")
        
        if response.status_code == 200:
            try:
                token_data = response.json()
                
                # Verify the access_token exists in the response
                if not token_data or "access_token" not in token_data:
                    print(f"Error: Response missing access_token: {response.text}")
                    # Handle specific known error cases
                    if "error" in token_data:
                        error_type = token_data.get("error")
                        if error_type == "invalid_client":
                            print("ERROR: Your Client ID or Client Secret is invalid. Please regenerate them in Zoho Developer Console.")
                            print("Go to: https://api-console.zoho.com/ and update your credentials.")
                        elif error_type == "invalid_code" or error_type == "invalid_grant":
                            print("ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                            print("To generate a new refresh token:")
                            print("1. Visit: http://localhost:5000/auth")
                            print("2. Follow the OAuth flow to get a new refresh token")
                            print("3. Update the ZOHO_REFRESH_TOKEN in your code")
                    return False
                
                ZOHO_TOKEN = token_data["access_token"]
                expires_in = token_data.get("expires_in", 3600)  # Default 1 hour
                
                # Update token expiry time (with 5-minute buffer)
                ZOHO_TOKEN_EXPIRY = datetime.now() + timedelta(seconds=expires_in - 300)
                
                # Update headers with new token
                ZOHO_HEADERS["Authorization"] = f"Zoho-oauthtoken {ZOHO_TOKEN}"
                
                print(f"Zoho token refreshed successfully: {ZOHO_TOKEN[:10]}..., expires in {expires_in} seconds")
                return True
            except (json.JSONDecodeError, TypeError, KeyError) as json_err:
                print(f"Error parsing token response: {str(json_err)}, Response: {response.text}")
                return False
        else:
            print(f"Failed to refresh token: {response.status_code} - {response.text}")
            if response.status_code == 400:
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        if error_data["error"] == "invalid_client":
                            print("ERROR: Your Client ID or Client Secret is invalid. Please regenerate them in Zoho Developer Console.")
                            print("Go to: https://api-console.zoho.com/ and update your credentials.")
                        elif error_data["error"] == "invalid_code" or error_data["error"] == "invalid_grant":
                            print("ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                            print("To generate a new refresh token:")
                            print("1. Visit: http://localhost:5000/auth")
                            print("2. Follow the OAuth flow to get a new refresh token")
                            print("3. Update the ZOHO_REFRESH_TOKEN in your code")
                except Exception:
                    pass
            return False
    except Exception as e:
        print(f"Error refreshing token: {str(e)}")
        return False

# Function to ensure token is valid before making API calls
def ensure_valid_token():
    global ZOHO_TOKEN, ZOHO_TOKEN_EXPIRY, ZOHO_HEADERS
    
    # Force a token refresh on first run or if token is expired
    if ZOHO_TOKEN is None or ZOHO_TOKEN_EXPIRY is None or datetime.now() >= ZOHO_TOKEN_EXPIRY:
        print("Token expired or first run, refreshing...")
        if not refresh_zoho_token():
            raise Exception("Failed to refresh Zoho token")
    
    return True

# Function to parse message with Grok API
def parse_with_grok(message):
    if not message:
        print("Error: No message provided")
        return {}
    
    # Format the prompt as a system and user message for chat completions API
    system_content = (
        "You are a financial transaction parser that extracts information into JSON format. "
        "Extract amount (number only), recipient (RAC or MC), and purpose. "
        "For recipient, normalize to 'RAC' or 'MC' (for MCAsie/Asie). Use null for missing info. "
        "Return ONLY valid JSON with no other text: {\"amount\":X,\"recipient\":Y,\"purpose\":Z}"
    )
    
    user_content = f"Parse this request: {message}"
    
    payload = {
        "model": "grok-2-latest",
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ],
        "max_tokens": 150,
        "temperature": 0.1  # Lower temperature for more predictable output
    }
    
    try:
        response = requests.post(GROK_API_URL, headers=GROK_HEADERS, json=payload)
        print(f"Status code: {response.status_code}")
        print(f"Raw response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            
            # Extract the content from the assistant's message
            if "choices" in result and result["choices"]:
                content = result["choices"][0].get("message", {}).get("content", "").strip()
                
                # Ensure we're only getting JSON by removing any surrounding text
                if "{" in content and "}" in content:
                    try:
                        json_start = content.find("{")
                        json_end = content.rfind("}") + 1
                        json_str = content[json_start:json_end]
                        parsed_data = json.loads(json_str)
                        
                        # Normalize numeric values
                        if parsed_data.get("amount") and not isinstance(parsed_data["amount"], (int, float)):
                            # Remove any non-numeric characters except decimal point
                            amount_str = ''.join(c for c in parsed_data["amount"] if c.isdigit() or c == '.')
                            if amount_str:
                                parsed_data["amount"] = amount_str
                        
                        return parsed_data
                    except json.JSONDecodeError:
                        print(f"Error: Could not parse JSON from response: {content}")
                        return {}
                else:
                    print(f"Error: No JSON found in response content: {content}")
            return {}
        else:
            print(f"Error: API returned status code {response.status_code}")
            return {}
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return {}

# Function to move funds to Cash in Transit in Zoho Books
def move_funds_to_cash_in_transit(amount, purpose):
    try:
        # Ensure we have a valid token before making the API call
        ensure_valid_token()
    except Exception as e:
        return {"code": -1, "message": f"Token validation failed: {str(e)}"}
    
    current_date = date.today().isoformat()
    reference_number = f"TRANSFER-{date.today().strftime('%Y%m%d')}-{int(datetime.now().timestamp()) % 10000}"
    
    # Format payload according to Zoho Books API documentation for bank transactions
    payload = {
        "date": current_date,
        "from_account_id": MC_CASH_ID,
        "to_account_id": CASH_IN_TRANSIT_ID,
        "amount": amount,
        "reference_number": reference_number,
        "description": f"Transfer for {purpose}",
        "transaction_type": "transfer_fund"  # Specify that this is a transfer transaction
    }
    
    print(f"Sending transfer request: {payload}")
    
    try:
        # Use the correct endpoint for bank transactions
        full_url = f"{ZOHO_API_URL}/banktransactions?organization_id={ZOHO_ORG_ID}"
        print(f"Sending request to URL: {full_url}")
        print(f"Using auth token: {ZOHO_TOKEN[:10]}...")
        
        # Add proper headers
        headers = {
            **ZOHO_HEADERS,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        
        response = requests.post(full_url, headers=headers, json=payload)
        print(f"Response status code: {response.status_code}")
        
        # Check if response is HTML (indicating a redirect)
        if response.headers.get('content-type', '').startswith('text/html'):
            print("Received HTML response instead of JSON - likely an authentication or endpoint issue")
            return {"code": -1, "message": "API request failed - received invalid response format"}
        
        # Try to get the response as JSON
        try:
            result = response.json()
            print(f"Response body: {json.dumps(result)[:200]}...")
        except Exception as e:
            print(f"Could not parse response as JSON: {str(e)}")
            return {"code": -1, "message": f"Invalid response format: {str(e)}"}
        
        # Check for HTTP errors
        if response.status_code >= 400:
            error_message = f"HTTP Error: {response.status_code}"
            if isinstance(result, dict):
                error_message += f" - {result.get('message', 'Unknown error')}"
            
            print(error_message)
            
            # Special handling of common errors
            if response.status_code == 401:
                error_message = "Authentication failed. Your Zoho token was rejected."
            elif response.status_code == 403:
                error_message = "Permission denied. Your Zoho token doesn't have the required permissions."
            elif response.status_code == 404:
                error_message = "API endpoint not found. Please check the Zoho Books API documentation."
            
            return {"code": response.status_code, "message": error_message}
        
        print(f"Zoho API Response: {result}")
        return result
        
    except requests.exceptions.RequestException as e:
        error_message = f"Request Error: {str(e)}"
        print(error_message)
        return {"code": -1, "message": error_message}

# Function to send Cliq message (placeholder)
def send_cliq_message(channel, text):
    print(f"To {channel}: {text}")  # Replace with actual Cliq API call

# Main logic to handle messages
def handle_message(message, sender):
    parsed = parse_with_grok(message)
    amount_str = parsed.get("amount")
    recipient = parsed.get("recipient")
    purpose = parsed.get("purpose")
    print(f"Parsed data: {parsed}")
    
    # Prepare response message
    response_text = ""
    
    # Check if we have minimum required information
    if not amount_str and not purpose:
        response_text = f"@{sender}: I couldn't understand your request. Please include an amount and purpose."
        send_cliq_message("Nicole", response_text)
        return {"status": "error", "text": response_text}
    
    # If we're missing just the amount
    if not amount_str:
        response_text = f"@{sender}: Please specify the amount to transfer for '{purpose}'."
        send_cliq_message("Nicole", response_text)
        return {"status": "error", "text": response_text}
    
    # If we're missing just the recipient
    if not recipient:
        response_text = f"@{sender}: Please specify who should receive the ${amount_str} for '{purpose}'."
        send_cliq_message("Nicole", response_text)
        return {"status": "error", "text": response_text}
    
    try:
        # Convert amount to float
        amount = float(amount_str)
        
        # Proceed with transfer
        result = move_funds_to_cash_in_transit(amount, purpose)
        
        if result.get("code") == 0:  # Zoho API success code
            # Get transaction ID if available
            transaction_id = ""
            if "banktransfer" in result:
                transaction_id = result["banktransfer"].get("banktransfer_id", "Unknown")
            
            # Success message
            response_text = f"@{sender}: Successfully transferred ${amount} to Cash in Transit for '{purpose}'. Transaction ID: {transaction_id}"
            send_cliq_message("Nicole", response_text)
            
            # Also notify recipient if RAC
            if recipient.upper() == "RAC":
                recipient_msg = f"RAC: {sender} sent ${amount} for '{purpose}'. Please confirm receipt."
                send_cliq_message("Nicole", recipient_msg)
                
            return {"status": "success", "text": response_text}
        else:
            # Error message
            error_msg = result.get("message", "Unknown error")
            response_text = f"@{sender}: Error moving funds: {error_msg}"
            send_cliq_message("Nicole", response_text)
            return {"status": "error", "text": response_text}
    except ValueError:
        response_text = f"@{sender}: Invalid amount format: '{amount_str}'. Please provide a valid number."
        send_cliq_message("Nicole", response_text)
        return {"status": "error", "text": response_text}

@app.route("/webhook", methods=["POST"])
def cliq_webhook():
    try:
        data = request.json
        print(f"Received webhook data: {data}")
        
        # Extract message and sender
        message = data.get("message")
        sender_id = data.get("sender_id")
        sender_name = data.get("sender_name", sender_id)
        
        if not message:
            print("Warning: No message found in request data")
            return {"status": "error", "text": "No message found in request"}
        
        if not sender_id and not sender_name:
            print("Warning: No sender information found in request data")
            sender_name = "Unknown User"
        
        # Process the message
        result = handle_message(message, sender_name or sender_id)
        
        # Return appropriate response based on processing result
        return result
    except Exception as e:
        error_message = f"Error processing webhook: {str(e)}"
        print(error_message)
        return {"status": "error", "text": error_message}

if __name__ == "__main__":
    # Check if we need to set up OAuth
    if not ZOHO_REFRESH_TOKEN or ZOHO_REFRESH_TOKEN == "1000.91c418adad92c23f178df1da76a7bac5.ca2a13216dcc884b3dd0b2b9359f1ed5":
        print("\nNo valid refresh token found. Starting OAuth setup...")
        if setup_zoho_auth():
            print("\nOAuth setup completed successfully!")
        else:
            print("\nOAuth setup failed. Please try again.")
            exit(1)
    
    # Start the main webhook server
    print("\nStarting webhook server...")
    app.run(port=CLIQ_WEBHOOK_PORT)