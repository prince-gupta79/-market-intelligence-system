
from sqlite3 import Time

import yfinance as yf
def get_market_pluse():
    print("Establishing secure link to Global Servvers")
    
    try:
        ticker = yf.Ticker("NEE")
        info = ticker.fast_info

        # this will help us to pull raw datas from market
        current_price = info['last_price']
        prev_close = info['regular_market_previous_close']
        
        # calculate the change by
        # formula ((current_prince - prev_price)/ previous)* 100
        price_change  = current_price - prev_close
        percent_change = (price_change / prev_close) * 100

        print(f"\n successful connection")
        print(f"NEE (NEE): ${current_price:,.2f}")
        print(f"24h chnage :${price_change:,.2f}({percent_change:.2f}%)")

        if percent_change > 0:
            print("MARKET IS BULLSHIT(upward trend)")
        
        else:
            print("MARKET IS BEARISH(downward trend)")

    except Exception as e:
        print(f"Error:{e}")
get_market_pluse()

import yfinance as yf
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style = "darkgrid")

def create_live_dashboard(ticker_symbol):
    print(f"Generating live Dashboard for {ticker_symbol}")

    # pulling 5 days of data at 1 hr interval
    data = yf.download(ticker_symbol, period = "5d", interval = "60m")

    # flatten multiindex and colomns names
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data.columns = data.columns.str.lower()


    if not data.empty:
        plt.figure(figsize=(12, 6))
        
        # plotting the close price
        plt.plot(data.index, 
                 data['close'], 
                 color = "#00ccffa1", linewidth = 2, label = 'Price(euro)')

        # adding labels n titles
        plt.title(f"Market Intelligence Report: {ticker_symbol}(last 5 days)", fontsize = 16, color = 'white')
        plt.xlabel("Time (UTC)", fontsize = 12, color = 'white')
        plt.ylabel("price(euro)", fontsize = 12, color='white')

        # terminal 
        plt.gcf().set_facecolor('#121212')
        plt.gca().set_facecolor('#121212')
        plt.xticks(rotation = 45, color = 'white')
        plt.yticks(color = 'white')

        plt.legend()
        plt.tight_layout()

        plt.savefig(f"{ticker_symbol}_market_report.png")
        print(f"Report saved successfully as '{ticker_symbol}_market_report.png'")
    else:
        print("Error: NO DATA FOUND ")

# running it for NEE
create_live_dashboard("NEE")