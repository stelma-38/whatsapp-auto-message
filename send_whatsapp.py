import os
from twilio.rest import Client
from datetime import datetime

# Récupération des secrets GitHub
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
to_whatsapp_number = os.environ["TWILIO_WHATSAPP_TO"]  # doit être au format international +33xxxxxxx

client = Client(account_sid, auth_token)

# Numéro Twilio Sandbox
from_whatsapp = "whatsapp:+14155238886"  

# Numéro destinataire (doit être inscrit dans Sandbox)
to_whatsapp = f"whatsapp:{to_whatsapp_number}"

# Message simple pour keep-alive
message_body = f"WhatsApp keep-alive ✅ {datetime.now().strftime('%d/%m/%Y %H:%M')}"

# Envoi du message
message = client.messages.create(
    from_=from_whatsapp,
    to=to_whatsapp,
    body=message_body
)

print("Message envoyé :", message.sid)
