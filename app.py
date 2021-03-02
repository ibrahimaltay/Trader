from views import run_method_with_perfect_intervals
from config import send_email

from models import fetch_btc_data_from_binance, create_btc_table_if_not_exists, \
create_altcoin_table_if_not_exists, fetch_altcoin_data_from_binance

def main():
    send_email("Bot is up and running!", "SUCCESS", "xrge152@gmail.com")

    try:
        print("Application Started!")
        create_btc_table_if_not_exists()
        create_altcoin_table_if_not_exists()
        run_method_with_perfect_intervals(fetch_btc_data_from_binance, 1)
    except Exception as e:
        send_email("The application stopped: " + str(e))


if __name__ == "__main__":
    main()