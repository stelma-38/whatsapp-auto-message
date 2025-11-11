# send_whatsapp.py
import os
from twilio.rest import Client
from datetime import datetime

# Récupération sécurisée des identifiants depuis les secrets GitHub
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token  = os.environ["TWILIO_AUTH_TOKEN"]
to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]   # format: whatsapp:+33xxxxxxxx

client = Client(account_sid, auth_token)

FROM_WHATSAPP = "whatsapp:+14155238886"   # Twilio Sandbox (ne pas modifier)
body = f"Rappel automatique : ({datetime.now().strftime('%d/%m/%Y %H:%M')})"

message = client.messages.create(
    from_=FROM_WHATSAPP,
    to=to_whatsapp,
    body=body
)

print("Message envoyé :", message.sid)
