import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application configuration
class Config:
    # Server settings
    PORT = int(os.getenv('PORT', 8080))
    HOST = os.getenv('HOST', '0.0.0.0')
    APP_URL = os.getenv('APP_URL', f'http://localhost:{PORT}')
    
    # Zoho credentials
    ZOHO_CLIENT_ID = os.getenv('ZOHO_CLIENT_ID')
    ZOHO_CLIENT_SECRET = os.getenv('ZOHO_CLIENT_SECRET')
    ZOHO_REFRESH_TOKEN = os.getenv('ZOHO_REFRESH_TOKEN')
    ZOHO_REDIRECT_URI = os.getenv('ZOHO_REDIRECT_URI')
    
    # Account IDs
    CASH_IN_TRANSIT_ACCOUNT = os.getenv('CASH_IN_TRANSIT_ACCOUNT')
    BE_BANK_ACCOUNT = os.getenv('BE_BANK_ACCOUNT')
    BELLISSIMA_BANK_ACCOUNT = os.getenv('BELLISSIMA_BANK_ACCOUNT')
    MCASIE_BANK_ACCOUNT = os.getenv('MCASIE_BANK_ACCOUNT')
    BDMS_BANK_ACCOUNT = os.getenv('BDMS_BANK_ACCOUNT')
    
    # Grok API
    GROK_API_KEY = os.getenv('GROK_API_KEY')
    
    # Zoho Cliq
    CLIQ_WEBHOOK_URL = os.getenv('CLIQ_WEBHOOK_URL')

# Logging configuration
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )
    
    # Set specific log levels for different modules
    logging.getLogger('werkzeug').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)
    
    return logging.getLogger(__name__)

# Initialize logging
logger = setup_logging() 