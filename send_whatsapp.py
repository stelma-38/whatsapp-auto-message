import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

from_whatsapp = "whatsapp:+14155238886"  # Sandbox Twilio
to_whatsapp = f"whatsapp:{os.environ['TWILIO_WHATSAPP_TO']}"
