from binance.client import Client
import sqlite3
import json

json_file = open('secrets.json', 'r')
parsed_json_file = json.load(json_file)

api_key = parsed_json_file.get('API_KEY')
api_secret = parsed_json_file.get('API_SECRET')

client = Client(api_key, api_secret)
conn = sqlite3.connect('coins.db')
c = conn.cursor()
