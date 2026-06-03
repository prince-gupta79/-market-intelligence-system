import yfinance as yf
import sqlite3
from datetime import datetime

SYMBOL = "NVDA"

conn = sqlite3.connect('market_intelligence.db')
cursor = conn.cursor()

# Step 1: check if price fetch works
ticker = yf.Ticker(SYMBOL)
current_price = ticker.fast_info['last_price']
print(f"Price fetched: {current_price}")
print(f"Price type: {type(current_price)}")  # ← this is key

# Step 2: try insert with explicit float conversion
try:
    cursor.execute(
        "INSERT INTO market_data (ticker, timestamp, price) VALUES (?, ?, ?)",
        (SYMBOL, str(datetime.now()), float(current_price))  # explicit float
    )
    conn.commit()
    print("Insert successful!")
except Exception as e:
    print(f"Insert failed: {e}")

conn.close()