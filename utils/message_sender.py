import requests
import json
from config import Config, logger

class CliqMessageSender:
    """Handles sending messages to Zoho Cliq"""
    
    def __init__(self):
        """Initialize the message sender"""
        self.webhook_url = Config.CLIQ_WEBHOOK_URL
        
        if not self.webhook_url:
            logger.warning("Zoho Cliq webhook URL not found in environment variables")
        elif not self.webhook_url.startswith("https://cliq.zoho.com"):
            logger.warning(f"Zoho Cliq webhook URL may be invalid: {self.webhook_url}")
    
    def send_message(self, channel, message):
        """Send a message to a Zoho Cliq channel"""
        if not self.webhook_url:
            logger.error("Zoho Cliq webhook URL not configured")
            # Instead of raising an exception, just log the message locally and continue
            logger.info(f"Would have sent to {channel}: {message}")
            return {"status": "not_sent", "reason": "webhook_not_configured"}
        
        try:
            # Log the message we're trying to send
            logger.info(f"Sending message to {channel}: {message[:100]}{'...' if len(message) > 100 else ''}")
            
            # Check the endpoint to determine the correct payload format
            if "/message" in self.webhook_url:
                # Format for /message endpoint
                payload = {
                    "text": message
                }
            else:
                # Format for /incoming endpoint (webhook)
                payload = {
                    "text": message
                }
            
            # Add debugging information
            logger.debug(f"Webhook URL: {self.webhook_url}")
            logger.debug(f"Payload: {payload}")
            
            # Send the message
            response = requests.post(
                self.webhook_url, 
                json=payload,
                headers={
                    "Content-Type": "application/json"
                }
            )
            
            # Log the response status, headers and body
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            
            try:
                response_body = response.json()
                logger.debug(f"Response body: {json.dumps(response_body)}")
            except:
                logger.debug(f"Response text: {response.text}")
            
            if response.status_code == 401:
                logger.error("Authentication error with Zoho Cliq webhook (401 Unauthorized)")
                logger.error("Please verify your webhook URL is correct and active")
                logger.error(f"Webhook URL: {self.webhook_url}")
                # Continue execution without raising an exception
                return {"status": "error", "reason": "authentication_failed"}
            
            if response.status_code == 400:
                logger.error("Bad request error with Zoho Cliq webhook (400 Bad Request)")
                logger.error("Please verify the payload format matches the API requirements")
                logger.error(f"Payload: {payload}")
                logger.error(f"Response: {response.text}")
                # Continue execution without raising an exception
                return {"status": "error", "reason": "bad_request"}
            
            # Only raise for non-handled error codes
            if response.status_code != 200 and response.status_code not in (400, 401):
                response.raise_for_status()
            
            # Log success
            if response.status_code == 200:
                logger.info(f"Message sent to channel {channel}")
                return response.json() if response.text else {"status": "success"}
            else:
                # For handled error codes, we've already logged the error but won't raise an exception
                logger.info(f"Message not sent due to API error")
                return {"status": "error", "reason": f"status_code_{response.status_code}"}
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending message to Zoho Cliq: {str(e)}")
            # Instead of raising, return error status
            return {"status": "error", "reason": str(e)}
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            # Instead of raising, return error status
            return {"status": "error", "reason": str(e)} 