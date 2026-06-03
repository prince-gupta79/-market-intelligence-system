# SMA = simple moving average

import sqlite3 
import pandas as pd

def calculate_trend(symbol):
    conn = sqlite3.connect('market_intelligence.db')

    query = f"SELECT price FROM market_data WHERE ticker = '{symbol}' ORDER BY timestamp ASC LIMIT 10"
    df = pd.read_sql_query(query, conn)
    conn.close()

    if len(df) < 2:
        print("Not enough data in the vault yet. keep your bot running")
        return
    
    # window=5 means its average of last 2
    df['SMA_2'] = df['price'].rolling(window=2).mean()

    latest_price = df['price'].iloc[-1]
    latest_sma = df['SMA_2'].iloc[-1]

    print(f"---- {symbol} TREND REPORT ----")
    print(f"Current Price: ${latest_price:.2f}")
    print(f"2-Day SMA: ${latest_sma:.2f}")

    # THE LOGIC ; is it a 'buy' or 'sell' signal
    if latest_price > latest_sma:
        print("SIGNAL : BULLSHIT (price is above average)")
    else:
        print("SIGNAL: bearish (price is below average)")

calculate_trend("NEE")