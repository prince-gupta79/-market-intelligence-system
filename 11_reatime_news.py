import yfinance as yf
import pandas as pd
import numpy as np

#1 getting raw data of gold
symbol = "GLD"
df = yf.download(symbol, period = "1y")

#2 adding technical signals
df['SMA_20'] = df['Close'].rolling(window = 20).mean()
df['Price_Return'] = df['Close'].squeeze().pct_change()

#3 simulating historical sentiments
# in a real world , we will pull this from a database of past news
# generating random sentiment betw. -0.5 & 0.5 to test the logic
np.random.seed(42)
df['Sentiment'] = np.random.uniform(-0.5, 0.5, size=len(df))

# the master logic
# we only buy if price > SMA & sentiment > 0.10
df['Signal'] = ((df['Close'].squeeze() > df['SMA_20']) & (df['Sentiment'] > 0.10)).astype(int)

# 5 calculating Returns
df['Strategy_Return'] = df['Signal'].shift(1) * df['Price_Return']
total_return = (df['Strategy_Return'] + 1).cumprod().iloc[-1].item()
market_return = (df['Close'].iloc[-1] / df['Close'].iloc[0]).item()

print(f" >>> {symbol} FUSION REPORT <<<<")
print(f"Market buy & hold: {market_return:.2f}x")
print(f"Sentiment-Aware Bot:{total_return:.2f}x")

if total_return  >  market_return:
    print(f"SUCCESS: the sentiment filter protected us & increased profitt")
else:
    print("LAGGING: the filter might br too strict. we missed some gains.")