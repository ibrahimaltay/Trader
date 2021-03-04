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
conn = sqlite3.connect('coins.db')
c = conn.cursor()

def send_email(Message, Destination):

    json_file = open('secrets.json', 'r')
    parsed_json_file = json.load(json_file)

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
        msg['Subject']=       subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(USERNAME, PASSWORD)
        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            conn.quit()

    except:
        sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message
