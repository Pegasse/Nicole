import requests
import json
from flask import Flask, request, redirect, url_for, session
from datetime import date, datetime, timedelta
import os
import webbrowser
import threading
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key-here')  # Required for session management

# Add debugging information at startup
print("====== TheBrain.py - Starting up ======")
print(f"Current working directory: {os.getcwd()}")

# Get the app URL from environment or construct from request
def get_app_url():
    if os.environ.get('APP_URL'):
        return os.environ.get('APP_URL')
    return request.host_url.rstrip('/') if request else 'http://localhost:8080'

# Grok API setup
GROK_API_URL = "https://api.x.ai/v1/chat/completions"  # Grok API URL
GROK_API_KEY = os.environ.get("GROK_API_KEY")  # Get from environment variable
GROK_HEADERS = {
    "Authorization": f"Bearer {GROK_API_KEY}",
    "Content-Type": "application/json",
}

# Zoho Books API setup
ZOHO_API_URL = "https://www.zohoapis.com/books/v3"
ZOHO_ORG_ID = os.environ.get("ZOHO_ORG_ID")  # Get from environment variable
print(f"Zoho organization ID: {ZOHO_ORG_ID}")

# Zoho OAuth configuration
ZOHO_CLIENT_ID = os.environ.get("ZOHO_CLIENT_ID")
ZOHO_CLIENT_SECRET = os.environ.get("ZOHO_CLIENT_SECRET")
ZOHO_SCOPE = "ZohoBooks.fullaccess.all"
ZOHO_REDIRECT_URI = os.environ.get("ZOHO_REDIRECT_URI")  # Get from environment variable

# Add your refresh token here - this is required for token refresh to work
ZOHO_REFRESH_TOKEN = os.environ.get("ZOHO_REFRESH_TOKEN")

# Report on credential status
print(f"Zoho Credentials Status:")
print(f"- Client ID: {'✓ Present' if ZOHO_CLIENT_ID else '✗ Missing'}")
print(f"- Client Secret: {'✓ Present' if ZOHO_CLIENT_SECRET else '✗ Missing'}")
print(f"- Refresh Token: {'✓ Present' if ZOHO_REFRESH_TOKEN else '✗ Missing'}")
print(f"- Redirect URI: {'✓ Present' if ZOHO_REDIRECT_URI else '✗ Missing'}")

# Current token and expiry
ZOHO_TOKEN = None
print("Initial access token: None (will be refreshed on first use)")
ZOHO_TOKEN_EXPIRY = datetime.now() - timedelta(minutes=5)

ZOHO_HEADERS = {
    "Content-Type": "application/json",
}

# Account IDs for the transfer
MC_CASH_ID = os.environ.get("MC_CASH_ID")
MC_BANK_ID = os.environ.get("MC_BANK_ID")
MC_MPESA_ID = os.environ.get("MC_MPESA_ID")
BE_CASH_ID = os.environ.get("BE_CASH_ID")
BE_BANK_ID = os.environ.get("BE_BANK_ID")
BE_MPESA_ID = os.environ.get("BE_MPESA_ID")
MCASIE_CASH_ID = os.environ.get("MCASIE_CASH_ID")
CASH_IN_TRANSIT_ID = os.environ.get("CASH_IN_TRANSIT_ID")
ROYALTIES_AVAILABLE_ID = os.environ.get("ROYALTIES_AVAILABLE_ID")
EXPENSE_PROVISIONS_ID = os.environ.get("EXPENSE_PROVISIONS_ID")
FOND_DE_CAISSE_ID = os.environ.get("FOND_DE_CAISSE_ID")
BUYING_PETTY_CASH_ID = os.environ.get("BUYING_PETTY_CASH_ID")

# Cliq webhook port
CLIQ_WEBHOOK_PORT = 5000

# Global variable to store the authorization code
auth_code = None

@app.route("/auth")
def auth():
    """Initiate the OAuth flow"""
    if not ZOHO_CLIENT_ID or not ZOHO_REDIRECT_URI:
        return "Error: Missing OAuth configuration", 500
    
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
    
    app_url = get_app_url()
    return f"""
    <h1>Zoho OAuth Setup</h1>
    <p>Click the button below to authorize the application:</p>
    <a href="{auth_url}" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; text-decoration: none; border-radius: 5px;">
        Authorize with Zoho
    </a>
    <p style="margin-top: 20px; color: #666;">
        After authorization, you'll receive a refresh token. Copy it and update the ZOHO_REFRESH_TOKEN environment variable in your DigitalOcean App Platform settings.
    </p>
    """

@app.route("/callback")
def callback():
    """Handle the OAuth callback from Zoho"""
    code = request.args.get("code")
    if not code:
        return "Error: No authorization code received", 400
    
    # Exchange the code for tokens
    result = get_refresh_token(code)
    if result:
        app_url = get_app_url()
        return f"""
        <h1>Success!</h1>
        <p>Your refresh token has been generated successfully.</p>
        <p>Please follow these steps:</p>
        <ol>
            <li>Copy the refresh token below</li>
            <li>Go to your DigitalOcean App Platform dashboard</li>
            <li>Select your app</li>
            <li>Go to Settings > Environment Variables</li>
            <li>Update the ZOHO_REFRESH_TOKEN variable with the new token</li>
            <li>Save the changes and redeploy your app</li>
        </ol>
        <p>Your refresh token:</p>
        <pre style="background-color: #f5f5f5; padding: 10px; border-radius: 5px;">{result['refresh_token']}</pre>
        <p>You can now close this window.</p>
        <script>window.close();</script>
        """
    else:
        return "Error: Failed to get refresh token", 500

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
                            app_url = get_app_url()
                            print(f"ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                            print(f"To generate a new refresh token:")
                            print(f"1. Visit: {app_url}/auth")
                            print(f"2. Follow the OAuth flow to get a new refresh token")
                            print(f"3. Update the ZOHO_REFRESH_TOKEN in your DigitalOcean App Platform environment variables")
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
                            app_url = get_app_url()
                            print(f"ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                            print(f"To generate a new refresh token:")
                            print(f"1. Visit: {app_url}/auth")
                            print(f"2. Follow the OAuth flow to get a new refresh token")
                            print(f"3. Update the ZOHO_REFRESH_TOKEN in your DigitalOcean App Platform environment variables")
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
        "You are a financial transaction parser for an organization with multiple business units and accounts. "
        "Extract the following information into JSON format:\n"
        "1. amount: (number only)\n"
        "2. from_account: The source account (options: MC Cash, MC Bank, MC Mpesa, BE Cash, BE Bank, BE Mpesa, MCAsie Cash, Cash In Transit, Royalties Available, Expense Provisions, Fond de Caisse, Buying Petty Cash)\n"
        "3. to_account: The destination account (same options as from_account)\n"
        "4. purpose: The reason for the transfer\n"
        "5. description: A brief summary of the transaction\n\n"
        "Special Rules:\n"
        "- If the from_account contains 'MC', the location is MicroConcept\n"
        "- If the from_account contains 'BE', the location is Bellissima\n"
        "- For transfers to MCAsie/RAC from any MC or BE account, automatically set to_account to 'Cash In Transit'\n"
        "- If destination is MCAsie/RAC but from_account isn't specified, assume 'Cash In Transit'\n"
        "- If from_account or to_account aren't clearly specified, set them to null\n"
        "- Normalize references to 'MCAsie', 'Asie', or 'RAC' as 'MCAsie Cash' for to_account\n"
        "- For withdrawals, if no to_account is specified, set it to a Cash account with a similar prefix to the from_account. For example, BE Bank to BE Cash\n\n"
        "Return ONLY valid JSON with no other text: {\"amount\":X,\"from_account\":Y,\"to_account\":Z,\"purpose\":P,\"description\":D}"
    )
    
    user_content = f"Parse this transfer request: {message}"
    
    payload = {
        "model": "grok-2-latest",
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ],
        "max_tokens": 200,
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
                                parsed_data["amount"] = float(amount_str)
                        
                        # Apply special transfer rules
                        if parsed_data.get("to_account") and any(x in str(parsed_data["to_account"]).upper() for x in ["MCASIE", "RAC", "ASIE"]):
                            if parsed_data.get("from_account") and any(x in str(parsed_data["from_account"]).upper() for x in ["MC ", "BE "]):
                                # For transfers from MC or BE to MCAsie, set to_account to Cash In Transit
                                parsed_data["to_account"] = "Cash In Transit"
                            elif not parsed_data.get("from_account"):
                                # If to_account is MCAsie but from_account isn't specified
                                parsed_data["from_account"] = "Cash In Transit"
                        
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
def move_funds_to_cash_in_transit(parsed_data):
    try:
        # Ensure we have a valid token before making the API call
        ensure_valid_token()
    except Exception as e:
        return {"code": -1, "message": f"Token validation failed: {str(e)}"}
    
    # Extract data from parsed result
    amount = parsed_data.get("amount")
    from_account = parsed_data.get("from_account", "MC Cash")  # Default to MC Cash if not specified
    to_account = parsed_data.get("to_account", "Cash In Transit")  # Default to Cash In Transit if not specified
    purpose = parsed_data.get("purpose", "Funds Transfer")
    description = parsed_data.get("description", f"Transfer for {purpose}")
    
    # Map account names to Zoho Books account IDs
    account_id_map = {
        "MC Cash": MC_CASH_ID,
        "MC Bank": MC_BANK_ID,
        "MC Mpesa": MC_MPESA_ID,
        "BE Cash": BE_CASH_ID,
        "BE Bank": BE_BANK_ID,
        "BE Mpesa": BE_MPESA_ID,
        "MCAsie Cash": MCASIE_CASH_ID,
        "Cash In Transit": CASH_IN_TRANSIT_ID,
        "Royalties Available": ROYALTIES_AVAILABLE_ID,
        "Expense Provisions": EXPENSE_PROVISIONS_ID,
        "Fond de Caisse": FOND_DE_CAISSE_ID,
        "Buying Petty Cash": BUYING_PETTY_CASH_ID
    }
    
    # Get account IDs
    from_account_id = account_id_map.get(from_account)
    to_account_id = account_id_map.get(to_account)
    
    # Validate account IDs
    if not from_account_id:
        return {"code": -1, "message": f"Unknown from account: {from_account}"}
    if not to_account_id:
        return {"code": -1, "message": f"Unknown to account: {to_account}"}
    
    current_date = date.today().isoformat()
    reference_number = f"TRANSFER-{date.today().strftime('%Y%m%d')}-{int(datetime.now().timestamp()) % 10000}"
    
    # Format payload according to Zoho Books API documentation for bank transactions
    payload = {
        "date": current_date,
        "from_account_id": from_account_id,
        "to_account_id": to_account_id,
        "amount": amount,
        "reference_number": reference_number,
        "description": description,
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
    print(f"Parsed data: {parsed}")
    
    # Prepare response message
    response_text = ""
    
    # Check if we have minimum required information
    if not parsed.get("amount"):
        response_text = f"@{sender}: I couldn't understand your request. Please include an amount to transfer."
        send_cliq_message("Nicole", response_text)
        return {"status": "error", "text": response_text}
    
    try:
        # Convert amount to float if it's not already
        if not isinstance(parsed.get("amount"), (int, float)):
            parsed["amount"] = float(parsed.get("amount"))
        
        # Proceed with transfer
        result = move_funds_to_cash_in_transit(parsed)
        
        if result.get("code") == 0:  # Zoho API success code
            # Get transaction ID if available
            transaction_id = ""
            if "banktransfer" in result:
                transaction_id = result["banktransfer"].get("banktransfer_id", "Unknown")
            
            # Extract accounts for message
            from_account = parsed.get("from_account", "MC Cash")
            to_account = parsed.get("to_account", "Cash In Transit")
            purpose = parsed.get("purpose", "")
            purpose_text = f" for '{purpose}'" if purpose else ""
            
            # Success message
            response_text = f"@{sender}: Successfully transferred ${parsed['amount']} from {from_account} to {to_account}{purpose_text}. Transaction ID: {transaction_id}"
            send_cliq_message("Nicole", response_text)
            
            # Also notify recipient if MCAsie/RAC
            if "MCAsie" in to_account or to_account == "Cash In Transit":
                recipient_msg = f"RAC: {sender} sent ${parsed['amount']} from {from_account} to {to_account}{purpose_text}. Please confirm receipt."
                send_cliq_message("Nicole", recipient_msg)
                
            return {"status": "success", "text": response_text}
        else:
            # Error message
            error_msg = result.get("message", "Unknown error")
            response_text = f"@{sender}: Error processing transfer: {error_msg}"
            send_cliq_message("Nicole", response_text)
            return {"status": "error", "text": response_text}
    except ValueError as e:
        response_text = f"@{sender}: Invalid amount format: '{parsed.get('amount')}'. Please provide a valid number."
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
    # Get the port from environment variable or use default
    port = int(os.environ.get("PORT", 8080))
    
    # Check if we need to set up OAuth
    if not ZOHO_REFRESH_TOKEN:
        print("\nNo valid refresh token found. Starting OAuth setup...")
        if refresh_zoho_token():
            print("\nOAuth setup completed successfully!")
        else:
            print("\nOAuth setup failed. Please try again.")
            exit(1)
    
    # Start the main webhook server
    print("\nStarting webhook server...")
    app.run(host='0.0.0.0', port=port)