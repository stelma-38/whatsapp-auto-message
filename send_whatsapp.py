import os
from datetime import datetime
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

to_whatsapp = os.environ["TWILIO_WHATSAPP_TO"]

now = datetime.now().strftime("%Y-%m-%d %H:%M")
message_body = f"Rappel automatique — envoyé le {now}"

message = client.messages.create(
    from_="whatsapp:+14155238886",
    to=f"whatsapp:{to_whatsapp}",
    content_sid="HX91e8b27459c3713448e8c12cd3f8c3e9",  # Template "hello_world"
    content_variables=f'{{"1":"{message_body}"}}'
)

print("Message envoyé via template :", message.sid)
