import os
from twilio.rest import Client
import twilioAPI

base_url = 'https://api.twilio.com/2010-04-01'
from boto.s3.connection import S3Connection

#account_sid = twilioAPI.get_account_sid()
account_sid = S3Connection(os.environ['TWILIO_ACC_SID'])
#auth_token = twilioAPI.get_auth_token()
auth_token = S3Connection(os.environ['TWILIO_AUTH_TOK'])
mes_sid = S3Connection(os.environ['TWILIO_GET_ME_SID'])
key = S3Connection(os.environ['TWILIO_KEY'])
client = Client(account_sid, auth_token)

def send_message(text, number):
    message = client.messages \
                    .create(
                        messaging_service_sid=mes_sid,
                        body= text,
                        to='+1' + str(number)
                    )
    print(text)
    print(message.sid)


def add_number(user, number):
    validation_request = client.validation_requests \
                                .create(
                                    friendly_name=user,
                                    phone_number='+1' + number
                                )
    print(validation_request.friendly_name)
