import os
from twilio.rest import Client
from datetime import datetime

# Récupération des secrets depuis GitHub Actions
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]  # ton numéro WhatsApp dans le sandbox
from_whatsapp = "whatsapp:+14155238886"  # numéro sandbox Twilio

client = Client(account_sid, auth_token)

# Message keepalive (on peut mettre n'importe quel texte court)
message_body = f"WhatsApp keepalive ✅ {datetime.now().strftime('%d/%m/%Y %H:%M')}"

# Envoi du message
message = client.messages.create(
    from_=from_whatsapp,
    to=to_whatsapp,
    body=message_body
)

print("Message envoyé :", message.sid)
