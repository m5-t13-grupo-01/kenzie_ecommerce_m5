import smtplib
from email.message import EmailMessage
import os


def send_email(destiny, title, message):
    EMAIL_ADDRESS = os.getenv("EMAIL_HOST_USER")
    EMAIL_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
    msg = EmailMessage()
    msg["Subject"] = str(title)
    msg["From"] = str(EMAIL_ADDRESS)
    msg["To"] = str(destiny)
    msg.set_content(message)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
