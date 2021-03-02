import pandas as pd
from config import client, conn, c

def create_btc_table_if_not_exists():
    c.execute("""

    CREATE TABLE IF NOT EXISTS BTC_Data (
        SYMBOL TEXT NOT NULL,
        priceChange REAL NOT NULL,
        priceChangePercent REAL NOT NULL,
        weightedAvgPrice REAL NOT NULL,
        prevClosePrice REAL NOT NULL,
        lastPrice REAL NOT NULL,
        lastQty REAL NOT NULL,
        bidPrice REAL NOT NULL,
        bidQty REAL NOT NULL,
        askPrice REAL NOT NULL,
        askQty REAL NOT NULL,
        openPrice REAL NOT NULL,
        highPrice REAL NOT NULL,
        lowPrice REAL NOT NULL,
        volume REAL NOT NULL,
        quoteVolume REAL NOT NULL,
        openTime REAL NOT NULL,
        closeTime REAL NOT NULL,
        firstId REAL NOT NULL,
        lastId REAL NOT NULL,
        count REAL NOT NULL
    );

    """)
def create_altcoin_table_if_not_exists():
        c.execute("""

    CREATE TABLE IF NOT EXISTS X_Data (
        SYMBOL TEXT NOT NULL,
        priceChange REAL NOT NULL,
        priceChangePercent REAL NOT NULL,
        weightedAvgPrice REAL NOT NULL,
        prevClosePrice REAL NOT NULL,
        lastPrice REAL NOT NULL,
        lastQty REAL NOT NULL,
        bidPrice REAL NOT NULL,
        bidQty REAL NOT NULL,
        askPrice REAL NOT NULL,
        askQty REAL NOT NULL,
        openPrice REAL NOT NULL,
        highPrice REAL NOT NULL,
        lowPrice REAL NOT NULL,
        volume REAL NOT NULL,
        quoteVolume REAL NOT NULL,
        openTime REAL NOT NULL,
        closeTime REAL NOT NULL,
        firstId REAL NOT NULL,
        lastId REAL NOT NULL,
        count REAL NOT NULL
    );

    """)

insert_btc_command = """ INSERT INTO BTC_Data VALUES 
(
:symbol, 
:priceChange,
:priceChangePercent,
:weightedAvgPrice, 
:prevClosePrice, 
:lastPrice,
:lastQty,
:bidPrice,
:bidQty,
:askPrice,
:askQty,
:openPrice,
:highPrice,
:lowPrice,
:volume,
:quoteVolume,
:openTime,
:closeTime,
:firstId,
:lastId,
:count
) """

insert_x_command = """

INSERT INTO X_Data VALUES 
(
:symbol, 
:priceChange,
:priceChangePercent,
:weightedAvgPrice, 
:prevClosePrice, 
:lastPrice,
:lastQty,
:bidPrice,
:bidQty,
:askPrice,
:askQty,
:openPrice,
:highPrice,
:lowPrice,
:volume,
:quoteVolume,
:openTime,
:closeTime,
:firstId,
:lastId,
:count
) 


"""

ticker = {'symbol': 'BTCUSDT',
 'priceChange': '-2895.51000000',
 'priceChangePercent': '-6.138',
 'weightedAvgPrice': '45456.53353644',
 'prevClosePrice': '47174.01000000',
 'lastPrice': '44278.52000000',
 'lastQty': '0.00304800',
 'bidPrice': '44278.52000000',
 'bidQty': '0.47646400',
 'askPrice': '44278.53000000',
 'askQty': '0.00506700',
 'openPrice': '47174.03000000',
 'highPrice': '47557.14000000',
 'lowPrice': '43556.98000000',
 'volume': '76126.88848800',
 'quoteVolume': '3460464459.57967261',
 'openTime': 1614436307565,
 'closeTime': 1614522707565,
 'firstId': 673680260,
 'lastId': 675468951,
 'count': 1788692}

def get_btc_as_dataframe():
    return pd.DataFrame(c.execute("""
    SELECT * FROM BTC_Data
    """).fetchall(), columns=ticker.keys())

def export_btc_as_dataframe():
    pd.DataFrame(c.execute("""
    SELECT * FROM BTC_Data
    """).fetchall(), columns=ticker.keys()).to_csv('BTC_Data.csv')

def delete_data_from_BTC():
    c.execute("DELETE FROM BTC_Data")
    conn.commit()

def fetch_btc_data_from_binance():
        c.execute(insert_btc_command, client.get_ticker(symbol='BTCUSDT'))
        conn.commit()

def fetch_altcoin_data_from_binance():
        c.execute(insert_x_command, client.get_ticker(symbol='XLMUSDT'))
        conn.commit()

if __name__ == '__main__':
    export_btc_as_dataframe()