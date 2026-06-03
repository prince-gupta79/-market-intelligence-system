import sqlite3
import yfinance as yf
from datetime import datetime

# creating a database file
conn = sqlite3.connect('market_intelligence.db')
cursor = conn.cursor()

# creating a table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS market_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ticker TEXT,
                    timestamp DATETIME,
                    price REAL
                )''')

def log_price(symbol):
    ticker = yf.Ticker(symbol)
    current_price = ticker.fast_info['last_price']
    now = datetime.now().strftime("%y-%m-%d %H:%M:%S")

    cursor.execute("INSERT INTO market_data (ticker, timestamp, price) VALUES(?,?,?)", (symbol, now, current_price))
    conn.commit()
    print(f"Logged {symbol} at ${current_price:.2f} to the vault.")

log_price("NVDA")
log_price("BTC-USD")
log_price("BTC-USD")
log_price("NEE")
log_price("NEE")
log_price("GS")
log_price("WOOF")
log_price("NEE")
conn.close()
