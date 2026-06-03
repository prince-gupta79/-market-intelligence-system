import pandas as pd
import yfinance as yf
import requests

# addin telegram bot
BOT_TOKEN = "8724582515:AAEElkYDy06wM70CR9m9dASomqENsgmZfuY" # replace with your bot token
CHAT_ID = "7965377966" # replace with your chat id

def send_telegram(message):
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
  requests.post(url, data={"chat_id":CHAT_ID, "text": message})

# getting a full year of history
df = yf.download("NVDA", period = "1y")

# flatten the multiIndex columns
df.columns = df.columns.get_level_values(0)

df['Daily_Returns'] = df['Close'].pct_change()

# calculating the signal 20-D avg
df['SMA_20'] = df['Close'].rolling(window=20).mean()

# creating the position 1 if price > SMA, 0 otherwise
df['signal'] = (df['Close'] > df['SMA_20']).astype(int)

# calculating the daily returns
df['strategy_returns'] = df['signal'].shift(1) * df['Daily_Returns']

# cumulative profits
total_market_return = (df['Daily_Returns'] + 1).cumprod().iloc[-1]
total_strategy_return = (df['strategy_returns'] + 1).cumprod().iloc[-1]

print(f" --- 1- YEAR PERFORMANCE BATTLE ---")
print(f"Buy & Hold Growth:{total_market_return:.2f}x")
print(f"Strategy Growth:{total_strategy_return:.2f}x")

if total_strategy_return > total_market_return:
    result = "THE BOT WONN! you beat the market"
else:
    result = "THE MARKET WONN! your bot needs better logic"

message = f"""
NVDA 1-year PERFORMANCE REPORT

Buy & Hold Growth : {total_market_return:.2f}x
Strategy Growth   : {total_strategy_return:.2f}x

{result}
      """
print(message)
send_telegram(message)
print("Message sent to telegram")