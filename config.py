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

# def send_email(text, subject, receiver):

#     msg = EmailMessage()
#     msg.set_content(text)
#     msg['Subject'] = subject
#     msg['From'] = "traderbot"
#     msg['To'] = receiver

#     server = smtplib.SMTP('smtp.google.com', 587)
#     server.starttls()
    
#     email = parsed_json_file.get('EMAIL')
#     email_password = parsed_json_file.get('EMAIL_PASSWORD')

#     server.login(email, email_password)
#     server.send_message(msg)
#     server.quit()