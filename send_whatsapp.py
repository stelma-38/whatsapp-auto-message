import os
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_="whatsapp:+14155238886",
    body="Whatsapp est toujours actif sur Twilio",
    to=f"whatsapp:{to_whatsapp}"
)

print("Message envoyé :", message.sid)
