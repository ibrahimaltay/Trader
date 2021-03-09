from binance.client import Client
import sqlite3
import json
import smtplib
from email.message import EmailMessage



json_file = open('secrets.json', 'r')
parsed_json_file = json.load(json_file)

api_key = parsed_json_file.get('API_KEY')
api_secret = parsed_json_file.get('API_SECRET')

client = Client(api_key, api_secret)


def send_email(Message, Destination):

    SMTPserver = 'mail.oyuncasusu.com'
    sender =     'trade@oyuncasusu.com'
    destination = Destination

    USERNAME = parsed_json_file.get('EMAIL')
    PASSWORD = parsed_json_file.get('EMAIL_PASSWORD')

    # typical values for text_subtype are plain, html, xml
    text_subtype = 'plain'

    content="""\
    Test message
    """

    subject="Notification"

    import sys
    import os
    import re

    from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
    # from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

    # old version
    # from email.MIMEText import MIMEText
    from email.mime.text import MIMEText

    try:
        msg = MIMEText(Message, text_subtype)
        msg['Subject']= subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all

        mail_conn = SMTP(SMTPserver)
        mail_conn.set_debuglevel(False)
        mail_conn.login(USERNAME, PASSWORD)
        try:
            mail_conn.sendmail(sender, destination, msg.as_string())
        finally:
            mail_conn.quit()

    except Exception as e:
        print(f"Email Exception: {str(e)}")
