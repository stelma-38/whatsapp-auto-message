import os
from datetime import datetime
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]

# Variables du template Twilio Sandbox (obligatoires)
date_str = datetime.now().strftime("%Y-%m-%d")
time_str = datetime.now().strftime("%H:%M")

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body=f"Your appointment is coming up on {date_str} at {time_str}",
    to=f"whatsapp:{to_whatsapp}"
)

print("Message envoyé :", message.sid)
