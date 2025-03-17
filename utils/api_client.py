import requests
import certifi
import ssl
import urllib3
from config import Config, logger

class GrokAPIClient:
    """Client for interacting with the Grok API"""
    
    def __init__(self):
        """Initialize the Grok API client"""
        self.api_key = Config.GROK_API_KEY
        # Using the official Grok API endpoint
        self.api_url = "https://api.grok.ai/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("Grok API key not found in environment variables")
        
        # Configure SSL settings for Heroku environment
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        # Create a session with Heroku-specific SSL configuration
        self.session = requests.Session()
        
        # Configure SSL context for Heroku
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        ssl_context.check_hostname = False  # Disable hostname checking for Heroku
        ssl_context.verify_mode = ssl.CERT_NONE  # Disable certificate verification for Heroku
        
        # Configure retry strategy with longer timeouts
        retry_strategy = urllib3.Retry(
            total=5,  # Increase total retries
            backoff_factor=2,  # Increase backoff factor
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        # Create custom adapter with SSL context
        adapter = requests.adapters.HTTPAdapter(
            max_retries=retry_strategy,
            pool_connections=10,
            pool_maxsize=10
        )
        
        # Mount the adapter with SSL context
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
        
        # Set SSL context for the session
        self.session.verify = False  # Disable SSL verification for Heroku
    
    def parse_message(self, message):
        """Parse a message using the Grok API"""
        if not self.api_key:
            raise Exception("Grok API key not configured")
        
        try:
            # Prepare the API request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "User-Agent": "NicoleBot/1.0",
                "Accept": "application/json"
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
            
            # Create the request payload
            payload = {
                "model": "grok-1",
                "messages": [
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": message}
                ],
                "temperature": 0.1,
                "max_tokens": 150
            }
            
            # Make the API request with SSL verification disabled
            response = self.session.post(
                self.api_url, 
                headers=headers, 
                json=payload,
                timeout=60,  # Increase timeout
                verify=False  # Disable SSL verification
            )
            
            # Log response status and headers for debugging
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            if "choices" not in result or not result["choices"]:
                raise Exception("No response from Grok API")
            
            # Extract the parsed data
            parsed_data = result["choices"][0]["message"]["content"]
            
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
            logger.error(f"Error making request to Grok API: {str(e)}")
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