import os
from twilio.rest import Client
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


class NotificationManager:
    def __init__(self):
        self.email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_EMAIL_PASSWORD"]
        self.client = Client(os.environ["ACCOUNT_SID"],os.environ["AUTH_TOKEN"])

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_ = os.environ["VIRTUAL_NUMBER"],
            body = message_body,
            to = "+918104145001"
        )

        print(message.sid)
    
    def send_email(self, email_body):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )



    