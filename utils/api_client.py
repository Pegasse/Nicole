import requests
from config import Config, logger

class GrokAPIClient:
    """Client for interacting with the Grok API"""
    
    def __init__(self):
        """Initialize the Grok API client"""
        self.api_key = Config.GROK_API_KEY
        self.api_url = "https://api.grok.ai/v1/chat/completions"
        
        if not self.api_key:
            logger.warning("Grok API key not found in environment variables")
    
    def parse_message(self, message):
        """Parse a message using the Grok API"""
        if not self.api_key:
            raise Exception("Grok API key not configured")
        
        try:
            # Prepare the API request
            headers = {
                "Authorization": f"Bearer {self.api_key}",
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
            
            # Make the API request
            response = requests.post(self.api_url, headers=headers, json=payload)
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
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to Grok API: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error parsing message: {str(e)}")
            raise 