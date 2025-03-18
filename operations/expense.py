import logging
from datetime import date
import requests
from config import Config, logger

class ExpenseHandler:
    def __init__(self, token_manager):
        self.token_manager = token_manager

    def process(self, parsed_data, sender_name):
        """Process the parsed expense data and create an expense in Zoho Books."""
        try:
            account_id = parsed_data["account_id"]
            amount = float(parsed_data["amount"])
            date_str = parsed_data.get("date", date.today().isoformat())
            reference = parsed_data.get("reference", "Expense")
            notes = parsed_data.get("notes", "")
            if not self.token_manager.ensure_valid_token():
                return {"status": "error", "text": "Failed to refresh Zoho API token"}
            headers = {
                "Authorization": f"Zoho-oauthtoken {self.token_manager.get_token()}",
                "Content-Type": "application/json"
            }
            url = f"{Config.ZOHO_API_URL}/expenses?organization_id={Config.ZOHO_ORG_ID}"
            payload = {
                "account_id": account_id,
                "amount": amount,
                "date": date_str,
                "reference_number": reference,
                "description": notes
            }
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 201:
                result = response.json()
                expense_id = result.get("expense", {}).get("expense_id", "Unknown")
                account_name = parsed_data.get("account_name", "Unknown")
                response_text = f"@{sender_name}: Successfully recorded expense of ${amount} to {account_name}. Expense ID: {expense_id}"
                logger.info(response_text)
                return {"status": "success", "text": response_text}
            else:
                error_msg = f"API Error ({response.status_code}): {response.text}"
                logger.error(error_msg)
                return {"status": "error", "text": error_msg}
        except Exception as e:
            error_msg = f"Error processing expense: {str(e)}"
            logger.error(error_msg)
            return {"status": "error", "text": error_msg}