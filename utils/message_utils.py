"""Message utility functions"""

def send_cliq_message(channel, text):
    """Send a message to Zoho Cliq - exact copy of old_brain.py implementation"""
    print(f"To {channel}: {text}")  # Replace with actual Cliq API call 