from twilio.rest import Client
import os

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

from_whatsapp = "whatsapp:+14155238886"  # Twilio sandbox
to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]

message = client.messages.create(
    from_=from_whatsapp,
    to=f"whatsapp:{to_whatsapp}",
    messaging_service_sid=None,  # si tu utilises sandbox, laisse None
    template="keep_alive"          # nom exact du template que tu as créé
)

print("Message envoyé :", message.sid)
