import os
from datetime import datetime
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]

# Message personnalisé inséré DANS le gabarit WhatsApp
now = datetime.now().strftime("%Y-%m-%d %H:%M")
message_body = f"Rappel automatique – message envoyé le {now}"

message = client.messages.create(
    from_="whatsapp:+14155238886",
    to=f"whatsapp:{to_whatsapp}",
    content_sid="HXae5b4f58e59eabd9c4f9d21c2b46e33e",  # TEMPLATE GRATUIT "survey"
    content_variables=f'{{"1":"{message_body}"}}'
)

print("Message envoyé via template :", message.sid)
