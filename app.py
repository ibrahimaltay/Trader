from models import create_table_if_not_exists, create_sqlite_db, fetch_crypto_data_from_binance
import time
import argparse
from datetime import datetime
from config import send_email

program_ticks = 0

MAIL_LIST = ['xrge152@gmail.com']

PARAMETER = 'BNBUSDT'

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("symbol")
args = arg_parser.parse_args()

if args.symbol:
    print(args.symbol)
    PARAMETER = str(args.symbol).upper()

conn, c = create_sqlite_db(PARAMETER)

def main():
    create_table_if_not_exists(PARAMETER, conn, c)
    fetch_crypto_data_from_binance(PARAMETER, PARAMETER, conn, c)
    datetime_now = datetime.now().astimezone().strftime("%d/%m/%Y %H:%M:%S")
    send_email(f"Successful execution at {datetime_now}", MAIL_LIST)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occured! \nStacktrace: {e}")
