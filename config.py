import os
import logging
from dotenv import load_dotenv

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Create a logger
logger = logging.getLogger('config')

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration settings for the API"""
    
    # X.ai API
    X_AI_API_KEY = os.getenv('X_AI_API_KEY', os.getenv('GROK_API_KEY'))
    
    # Flask app configuration
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
    PORT = int(os.getenv('PORT', 8080))
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY', 'your-secret-key-here')
    
    # Zoho Books API 
    ZOHO_API_URL = "https://www.zohoapis.com/books/v3"
    ZOHO_ORG_ID = os.getenv("ZOHO_ORG_ID")
    
    # Zoho OAuth
    ZOHO_CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
    ZOHO_CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
    ZOHO_SCOPE = "ZohoBooks.fullaccess.all"
    ZOHO_REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI")
    ZOHO_REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
    
    # App URL
    APP_URL = os.getenv('APP_URL')
    
    # Account IDs
    MC_CASH_ID = os.getenv("MC_CASH_ID")
    MC_BANK_ID = os.getenv("MC_BANK_ID")
    MC_MPESA_ID = os.getenv("MC_MPESA_ID")
    BE_CASH_ID = os.getenv("BE_CASH_ID")
    BE_BANK_ID = os.getenv("BE_BANK_ID")
    BE_MPESA_ID = os.getenv("BE_MPESA_ID")
    MCASIE_CASH_ID = os.getenv("MCASIE_CASH_ID")
    CASH_IN_TRANSIT_ID = os.getenv("CASH_IN_TRANSIT_ID")
    ROYALTIES_AVAILABLE_ID = os.getenv("ROYALTIES_AVAILABLE_ID")
    EXPENSE_PROVISIONS_ID = os.getenv("EXPENSE_PROVISIONS_ID")
    FOND_DE_CAISSE_ID = os.getenv("FOND_DE_CAISSE_ID")
    BUYING_PETTY_CASH_ID = os.getenv("BUYING_PETTY_CASH_ID")
    
    # Location IDs
    MICROCONCEPT_ID = os.getenv("MICROCONCEPT_ID")
    BELLISSIMA_ID = os.getenv("BELLISSIMA_ID")
    MCASIE_ID = os.getenv("MCASIE_ID")
    BDMS_ID = os.getenv("BDMS_ID")

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