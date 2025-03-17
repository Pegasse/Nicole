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
    ZOHO_ORG_ID = os.getenv('ZOHO_ORG_ID')  # Added organization ID
    
    # Account IDs from old_brain.py
    # MicroConcept accounts
    MC_CASH_ID = os.getenv('MC_CASH_ID')
    MC_BANK_ID = os.getenv('MC_BANK_ID')
    MC_MPESA_ID = os.getenv('MC_MPESA_ID')
    
    # Bellissima accounts
    BE_CASH_ID = os.getenv('BE_CASH_ID')
    BE_BANK_ID = os.getenv('BE_BANK_ID')
    BE_MPESA_ID = os.getenv('BE_MPESA_ID')
    
    # MCAsie accounts
    MCASIE_CASH_ID = os.getenv('MCASIE_CASH_ID')
    
    # Special accounts
    CASH_IN_TRANSIT_ID = os.getenv('CASH_IN_TRANSIT_ID')
    ROYALTIES_AVAILABLE_ID = os.getenv('ROYALTIES_AVAILABLE_ID')
    EXPENSE_PROVISIONS_ID = os.getenv('EXPENSE_PROVISIONS_ID')
    FOND_DE_CAISSE_ID = os.getenv('FOND_DE_CAISSE_ID')
    BUYING_PETTY_CASH_ID = os.getenv('BUYING_PETTY_CASH_ID')
    
    # Location IDs (for branch_id parameter)
    MICROCONCEPT_ID = os.getenv('MICROCONCEPT_ID')
    BELLISSIMA_ID = os.getenv('BELLISSIMA_ID')
    MCASIE_ID = os.getenv('MCASIE_ID')
    BDMS_ID = os.getenv('BDMS_ID')
    
    # Legacy account IDs (keeping for compatibility)
    CASH_IN_TRANSIT_ACCOUNT = os.getenv('CASH_IN_TRANSIT_ACCOUNT', os.getenv('CASH_IN_TRANSIT_ID'))
    BE_BANK_ACCOUNT = os.getenv('BE_BANK_ACCOUNT', os.getenv('BE_BANK_ID'))
    BELLISSIMA_BANK_ACCOUNT = os.getenv('BELLISSIMA_BANK_ACCOUNT', os.getenv('BE_BANK_ID'))
    MCASIE_BANK_ACCOUNT = os.getenv('MCASIE_BANK_ACCOUNT', os.getenv('MCASIE_CASH_ID'))
    BDMS_BANK_ACCOUNT = os.getenv('BDMS_BANK_ACCOUNT', os.getenv('BDMS_ID'))
    
    # X.ai API
    GROK_API_KEY = os.getenv('X_AI_API_KEY', os.getenv('GROK_API_KEY'))  # Support both names
    
    # Zoho Cliq
    CLIQ_WEBHOOK_URL = os.getenv('CLIQ_WEBHOOK_URL')
    ZOHO_BOT_TOKEN = os.getenv('ZOHO_BOT_TOKEN')  # Added for direct bot API access

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