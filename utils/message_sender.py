import requests
from config import Config, logger

class CliqMessageSender:
    """Handles sending messages to Zoho Cliq"""
    
    def __init__(self):
        """Initialize the message sender"""
        self.webhook_url = Config.CLIQ_WEBHOOK_URL
        
        if not self.webhook_url:
            logger.warning("Zoho Cliq webhook URL not found in environment variables")
    
    def send_message(self, channel, message):
        """Send a message to a Zoho Cliq channel"""
        if not self.webhook_url:
            raise Exception("Zoho Cliq webhook URL not configured")
        
        try:
            # Prepare the message payload
            payload = {
                "channel": channel,
                "message": message
            }
            
            # Send the message
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            
            # Log success
            logger.info(f"Message sent to channel {channel}")
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            logger.error(f"Error sending message to Zoho Cliq: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            raise 