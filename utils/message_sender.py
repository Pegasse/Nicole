import requests
import json
import logging
from config import Config, logger

class CliqMessageSender:
    """Handles sending messages to Zoho Cliq"""
    
    def __init__(self):
        """Initialize the message sender"""
        self.bot_token = Config.ZOHO_BOT_TOKEN
        self.cliq_enabled = bool(self.bot_token)
        
        # Check if Cliq integration is actually enabled
        if not self.cliq_enabled:
            logger.warning("⚠️ Zoho Cliq integration DISABLED - messages will be logged but not sent")
            logger.warning("To enable Cliq integration, set ZOHO_BOT_TOKEN in your DigitalOcean environment variables")
        else:
            logger.info("✅ Zoho Cliq integration ENABLED - messages will be sent to Cliq")
    
    def send_message(self, channel, text):
        """Send a message to Zoho Cliq (or just log it)"""
        # Always log the message locally, exactly like old_brain.py does
        logger.info(f"[TO {channel}]: {text}")
        
        # If integration is disabled, just log and return
        if not self.cliq_enabled:
            return {"status": "logged_only"}
            
        try:
            # Use the bot token for authentication
            headers = {
                "Authorization": f"Zoho-oauthtoken {self.bot_token}",
                "Content-Type": "application/json"
            }
            
            # Basic payload for the message
            payload = {"text": text}
            
            # Send the message using the bot token
            response = requests.post(
                "https://cliq.zoho.com/api/v2/bots/message", 
                json=payload,
                headers=headers,
                timeout=5
            )
            
            # Check if it worked
            if response.status_code == 200:
                logger.info(f"Message sent to channel {channel}")
                return {"status": "success"}
            else:
                logger.error(f"Failed to send message: {response.status_code} - {response.text}")
                return {"status": "error"}
            
        except Exception as e:
            logger.error(f"Error sending message: {str(e)}")
            # Don't raise the error, just log it
            return {"status": "error", "error": str(e)} 