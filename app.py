from views import run_method_with_perfect_intervals

from models import fetch_btc_data_from_binance, create_btc_table_if_not_exists, \
create_altcoin_table_if_not_exists, fetch_altcoin_data_from_binance

from config import send_email

import time

program_ticks = 0

MAIL_LIST = ['xrge152@gmail.com', 'sinatalay@hotmail.com']

def main():
    
    # send_email("Bot is up and running!", "SUCCESS", "xrge152@gmail.com, sinatalay@hotmail.com")
    
    print("Application Started!")
    
    send_email("Raspberry Pi is up and running!", MAIL_LIST)

    create_btc_table_if_not_exists()
    create_altcoin_table_if_not_exists()
    run_method_with_perfect_intervals(fetch_btc_data_from_binance, 1)

    program_ticks = 0

if __name__ == "__main__":
    
    while True:
        try:
            main()
        except Exception as e:
            send_email(e, MAIL_LIST)
            program_ticks += 1
            time.sleep(120)

        if program_ticks >= 10:
            break