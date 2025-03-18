import requests
import json
from datetime import datetime, timedelta
from config import Config, logger

class ZohoTokenManager:
    """Manages OAuth tokens for Zoho API access"""
    
    def __init__(self):
        """Initialize the token manager"""
        self.client_id = Config.ZOHO_CLIENT_ID
        self.client_secret = Config.ZOHO_CLIENT_SECRET
        self.refresh_token = Config.ZOHO_REFRESH_TOKEN
        self.redirect_uri = Config.ZOHO_REDIRECT_URI
        self.scope = "ZohoBooks.fullaccess.all"
        
        # Current token and expiry
        self.access_token = None
        self.token_expiry = datetime.now() - timedelta(minutes=5)  # Expired by default
        
        logger.info(f"Zoho Credentials Status:")
        logger.info(f"- Client ID: {'✓ Present' if self.client_id else '✗ Missing'}")
        logger.info(f"- Client Secret: {'✓ Present' if self.client_secret else '✗ Missing'}")
        logger.info(f"- Refresh Token: {'✓ Present' if self.refresh_token else '✗ Missing'}")
        logger.info(f"- Redirect URI: {'✓ Present' if self.redirect_uri else '✗ Missing'}")
    
    def get_token(self):
        """Get the current access token"""
        return self.access_token
    
    def initialize_oauth_flow(self):
        """Generate the OAuth authorization URL"""
        if not self.client_id or not self.redirect_uri:
            return "Error: Missing OAuth configuration", 500
        
        # Generate the authorization URL
        auth_url = "https://accounts.zoho.com/oauth/v2/auth"
        params = {
            "response_type": "code",
            "client_id": self.client_id,
            "scope": self.scope,
            "redirect_uri": self.redirect_uri,
            "access_type": "offline",
            "prompt": "consent"
        }
        auth_url = f"{auth_url}?{'&'.join(f'{k}={v}' for k,v in params.items())}"
        
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
    
    def handle_oauth_callback(self, code):
        """Exchange authorization code for refresh token"""
        token_url = "https://accounts.zoho.com/oauth/v2/token"
        data = {
            "grant_type": "authorization_code",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
            "redirect_uri": self.redirect_uri
        }
        
        try:
            response = requests.post(token_url, data=data)
            response.raise_for_status()
            result = response.json()
            
            if "refresh_token" in result:
                logger.info("\nSuccess! Tokens received")
                
                # Update tokens
                self.refresh_token = result['refresh_token']
                self.access_token = result['access_token']
                expires_in = result.get('expires_in', 3600)
                self.token_expiry = datetime.now() + timedelta(seconds=expires_in - 300)
                
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
                logger.error(f"Error: No refresh token in response: {result}")
                return "Error: Failed to get refresh token", 500
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request: {e}")
            if hasattr(e.response, 'text'):
                logger.error(f"Response: {e.response.text}")
            return "Error: Failed to get refresh token", 500
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing response: {e}")
            logger.error(f"Raw response: {response.text}")
            return "Error: Failed to get refresh token", 500
    
    def refresh_access_token(self):
        """Refresh the access token using the refresh token"""
        if not self.client_id or not self.client_secret or not self.refresh_token:
            logger.error(f"Error: Missing Zoho OAuth credentials. Client ID: {'✓' if self.client_id else '✗'}, Client Secret: {'✓' if self.client_secret else '✗'}, Refresh Token: {'✓' if self.refresh_token else '✗'}")
            return False
        
        try:
            logger.info(f"Attempting to refresh token...")
            refresh_url = "https://accounts.zoho.com/oauth/v2/token"
            payload = {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "refresh_token": self.refresh_token,
                "grant_type": "refresh_token"
            }
            
            # Debug info for the request
            logger.debug(f"Token refresh request details:")
            logger.debug(f"- URL: {refresh_url}")
            logger.debug(f"- Client ID: {self.client_id[:8]}...")
            logger.debug(f"- Client Secret: {self.client_secret[:8]}...")
            logger.debug(f"- Refresh Token: {self.refresh_token[:8]}...")
            
            response = requests.post(refresh_url, data=payload)
            logger.info(f"Refresh token response: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    token_data = response.json()
                    
                    # Verify the access_token exists in the response
                    if not token_data or "access_token" not in token_data:
                        logger.error(f"Error: Response missing access_token: {response.text}")
                        
                        # Handle specific known error cases
                        if "error" in token_data:
                            error_type = token_data.get("error")
                            if error_type == "invalid_client":
                                logger.error("ERROR: Your Client ID or Client Secret is invalid. Please regenerate them in Zoho Developer Console.")
                            elif error_type == "invalid_code" or error_type == "invalid_grant":
                                logger.error(f"ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                                logger.error(f"To generate a new refresh token, visit: {Config.APP_URL}/auth")
                        return False
                    
                    self.access_token = token_data["access_token"]
                    expires_in = token_data.get("expires_in", 3600)  # Default 1 hour
                    
                    # Update token expiry time (with 5-minute buffer)
                    self.token_expiry = datetime.now() + timedelta(seconds=expires_in - 300)
                    
                    logger.info(f"Zoho token refreshed successfully, expires in {expires_in} seconds")
                    return True
                except (json.JSONDecodeError, TypeError, KeyError) as json_err:
                    logger.error(f"Error parsing token response: {str(json_err)}, Response: {response.text}")
                    return False
            else:
                logger.error(f"Failed to refresh token: {response.status_code} - {response.text}")
                if response.status_code == 400:
                    try:
                        error_data = response.json()
                        if "error" in error_data:
                            if error_data["error"] == "invalid_client":
                                logger.error("ERROR: Your Client ID or Client Secret is invalid. Please regenerate them in Zoho Developer Console.")
                            elif error_data["error"] == "invalid_code" or error_data["error"] == "invalid_grant":
                                logger.error(f"ERROR: Your Refresh Token is invalid or expired. Please generate a new one.")
                                logger.error(f"To generate a new refresh token, visit: {Config.APP_URL}/auth")
                    except Exception:
                        pass
                return False
        except Exception as e:
            logger.error(f"Error refreshing token: {str(e)}")
            return False
    
    def ensure_valid_token(self):
        """Ensure we have a valid access token, refreshing if necessary"""
        # Force a token refresh on first run or if token is expired
        if self.access_token is None or self.token_expiry is None or datetime.now() >= self.token_expiry:
            logger.info("Token expired or first run, refreshing...")
            if not self.refresh_access_token():
                raise Exception("Failed to refresh Zoho token")
        
        return True 

    def get_expense_accounts(self):
        """Fetch the list of expense accounts from Zoho Books."""
        if not self.ensure_valid_token():
            raise Exception("Failed to get valid token")
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.get_token()}",
            "Content-Type": "application/json"
        }
        url = f"{Config.ZOHO_API_URL}/chartofaccounts?organization_id={Config.ZOHO_ORG_ID}&account_type=expense"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("chartofaccounts", [])
        else:
            logger.error(f"Failed to fetch expense accounts: {response.text}")
            return []

    def get_asset_accounts(self):
        """
        Fetch cash and bank accounts from Zoho Books.
        Returns a list of account objects.
        """
        logger.info(f"Fetching cash and bank accounts from Zoho")
        
        # Ensure we have a valid token
        if not self.ensure_valid_token():
            logger.error("Failed to get valid token for asset accounts")
            return []
        
        # Fetch cash accounts
        cash_accounts = self.get_accounts_by_type("cash")
        
        # Fetch bank accounts
        bank_accounts = self.get_accounts_by_type("bank")
        
        # Fetch other_asset accounts
        other_asset_accounts = self.get_accounts_by_type("other_asset")
        
        # Combine all asset accounts
        accounts = cash_accounts + bank_accounts + other_asset_accounts
        
        logger.info(f"Combined {len(cash_accounts)} cash, {len(bank_accounts)} bank, and {len(other_asset_accounts)} other asset accounts, total: {len(accounts)}")
        
        if accounts:
            # Log some account names for debugging
            account_names = [acc.get('account_name', 'unnamed') for acc in accounts[:5]]
            logger.info(f"Sample account names: {account_names}")
        else:
            logger.warning("No cash or bank accounts found from API")
            
        return accounts

    def get_accounts_by_type(self, account_type):
        """Fetch accounts of a specific type from Zoho Books API with detailed error checking."""
        if not self.ensure_valid_token():
            raise Exception(f"Failed to get valid token for fetching {account_type} accounts")
            
        url = f"{Config.ZOHO_API_URL}/chartofaccounts?organization_id={Config.ZOHO_ORG_ID}&account_type={account_type}"
        headers = {
            "Authorization": f"Zoho-oauthtoken {self.get_token()}",
            "Content-Type": "application/json"
        }
        
        logger.info(f"Fetching {account_type} accounts from Zoho Books API: {url}")
        
        try:
            response = requests.get(url, headers=headers)
            logger.info(f"{account_type} accounts API response: Status {response.status_code}")
            
            if response.status_code == 200:
                data = response.json()
                if "chartofaccounts" in data:
                    accounts = data["chartofaccounts"]
                    logger.info(f"Successfully fetched {len(accounts)} {account_type} accounts")
                    
                    # Add account_type field to each account for reference
                    for acc in accounts:
                        acc["account_type"] = account_type
                        
                    return accounts
                else:
                    logger.warning(f"No {account_type} accounts found in response: {data}")
                    return []
            else:
                logger.error(f"Failed to fetch {account_type} accounts: {response.status_code} - {response.text}")
                return []
        except Exception as e:
            logger.error(f"Error fetching {account_type} accounts: {str(e)}")
            return [] 