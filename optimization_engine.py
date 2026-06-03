# BACKTESTING//

import pandas as pd
import yfinance as yf
import requests

# addin telegram bot
BOT_TOKEN = "8724582515:AAEElkYDy06wM70CR9m9dASomqENsgmZfuY" # replace with your bot token
CHAT_ID = "7965377966" # replace with your chat id

def send_telegram(message):
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  requests.post(url, data={"chat_id":CHAT_ID, "text": message})


# setting up
df = yf.download("NVDA", period  = "1y")
df.columns = df.columns.get_level_values(0)
df['Daily_Returns'] = df['Close'].pct_change()

results = []

print("Running 98 simulations... pls wait")

# The Brute Force loop
for window in range(2, 100):
   #  calculating SMA for this specific window
   sma = df['Close'].rolling(window = window).mean()

   # generate signal: 1 if price > SMA, else 0
   signal = (df['Close'] > sma).astype(int).shift(1)

   # calcularting strategy return
   strategy_return = (signal * df['Daily_Returns'] + 1).cumprod().iloc[-1]

   # # storing the results 
   results.append({'Window' : window, 'Return': strategy_return})

# analyzing the results
results_df = pd.DataFrame(results)
best_run = results_df.loc[results_df['Return'].idxmax()]

print("\n >>> OPTIMIZATION COMPLETED >>>")
print(f"best window: {int(best_run['Window'])}days")
print(f"best returns: {best_run['Return']:.2f}x")
buy_and_hold = (df['Daily_Returns'] + 1).cumprod().iloc[-1]
print(f"buy & hold was: {buy_and_hold:.2f}x")

if best_run['Return'] > buy_and_hold:
   print("ME_WOOWWW YOU FIND A WINDOW THAT BEATS THE MARKET")
else:
   print("Even at its best, the market is stronger. we might need a different indicator...")

message = f"""
NVDA OPTIMIZATION REPORT

best sma window : {int(best_run['Window'])} days
best strategy return : {best_run['Return']:.2f}x
Strategy Growth   : {buy_and_hold:.2f}x
"""

print(message)
send_telegram(message)
print("Message sent to telegram")