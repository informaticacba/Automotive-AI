"""
This module loads environment variables from a .env file.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GRAPH_EMAIL_ADDRESS = os.getenv("GRAPH_EMAIL_ADDRESS")
GRAPH_CLIENT_ID = os.getenv("GRAPH_CLIENT_ID")
GRAPH_CLIENT_SECRET = os.getenv("GRAPH_CLIENT_SECRET")
GRAPH_TENANT_ID = os.getenv("GRAPH_TENANT_ID")
SERIAL_PORT = os.getenv("SERIAL_PORT")
baud_rate_str = os.getenv("BAUD_RATE")
if baud_rate_str is None:
    raise ValueError("BAUD_RATE environment variable is not set")
BAUD_RATE = int(baud_rate_str)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_PHONE_NUMBER = os.getenv("TWILIO_FROM_PHONE_NUMBER")
TEXT_TO_PHONE_NUMBER = os.getenv("TEXT_TO_PHONE_NUMBER")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_APP_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")
GOOGLE_CUSTOM_SEARCH_ID = os.getenv("GOOGLE_CUSTOM_SEARCH_ID")
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
EMAIL_PROVIDER = os.getenv("EMAIL_PROVIDER")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
