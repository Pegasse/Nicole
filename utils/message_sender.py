import requests
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
            
            # Prepare the message payload according to Zoho Cliq webhook format
            payload = {
                "message": {
                    "text": message,
                    "type": "text"
                },
                "channel": channel,
                "bot": {
                    "name": "Nicole"
                }
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
            
            # Log the response status and headers
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            
            if response.status_code == 401:
                logger.error("Authentication error with Zoho Cliq webhook (401 Unauthorized)")
                logger.error("Please verify your webhook URL is correct and active")
                logger.error(f"Webhook URL: {self.webhook_url}")
                # Continue execution without raising an exception
                return {"status": "error", "reason": "authentication_failed"}
            
            # Only raise for non-401 errors
            if response.status_code != 200 and response.status_code != 401:
                response.raise_for_status()
            
            # Log success
            if response.status_code == 200:
                logger.info(f"Message sent to channel {channel}")
                return response.json()
            else:
                # For 401 errors, we've already logged the error but won't raise an exception
                logger.info(f"Message not sent due to authentication error")
                return {"status": "error", "reason": "authentication_failed"}
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending message to Zoho Cliq: {str(e)}")
            # Instead of raising, return error status
            return {"status": "error", "reason": str(e)}
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            # Instead of raising, return error status
            return {"status": "error", "reason": str(e)} 