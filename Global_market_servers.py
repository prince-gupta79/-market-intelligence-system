import yfinance as yf
import pandas as pd
import time

def get_live_data():
    # we are putting bitcoin in usd
    print("connecting to Global Market Servers")

    try:
        # Fetching the ticker object
        ticker = yf.Ticker("BTC-USD")
        #  real time snapshot
        price = ticker.fast_info['last_price']
        change = ticker.fast_info['day_change']

        print(f"\n successful connection")
        print(f"live BITCOIN price : ${price:,.2f}")
        print(f"24h change : {change:.2f}%")

        return price
    except Exception as e:
        print(f"ERROR :{e}")

get_live_data()

import yfinance as yf

ticker = yf.Ticker("BTC-USD")

# this will be search light for DS 
print("Avaliable keys in Fast_info:")
print(list(ticker.fast_info.keys()))

import yfinance as yf
def get_market_pluse():
    print("Establishing secure link to Global Servvers")
    
    try:
        ticker = yf.Ticker("BTC-USD")
        info = ticker.fast_info

        # this will help us to pull raw datas from market
        current_price = info['last_price']
        prev_close = info['regular_market_previous_close']
        
        # calculate the change by
        # formula ((current_prince - prev_price)/ previous)* 100
        price_change  = current_price - prev_close
        percent_change = (price_change / prev_close) * 100

        print(f"\n successful connection")
        print(f"BITCOIN (BTC-USD): ${current_price:,.2f}")
        print(f"24h chnage :${price_change:,.2f}({percent_change:.2f}%)")

        if percent_change > 0:
            print("MARKET IS BULLISH(upward trend)")
        
        else:
            print("MARKET IS BEARISH(downward trend)")

    except Exception as e:
        print(f"Error:{e}")
get_market_pluse()