# in here im gonna show a crossover between
# price > SMA: 'buy/bullish'
# price < SMA: 'sell/bearish'

import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def plot_expert_crossover(symbol):

    # fetch 1 month of data 
    df = yf.download(symbol, period="1mo", interval="1d")

    # calculate the 5-day moving average
    df['SMA_2'] = df['Close'].rolling(window=2).mean()

    # creating visualization 
    plt.figure(figsize=(14, 7))
    sns.set_style("dark")
    plt.gca().set_facecolor("#1e1e1e")

# plotting the raw noise of price
    plt.plot(df.index, df['Close'], label='Actual Price', color = '#8884d8', alpha = 0.5, linewidth = 1)

    # plotting the mopving average(signal)
    plt.plot(df.index, df['SMA_2'], label = '5-Day Average(Trend)', color = '#ff7300', linewidth = 1)
   
    plt.title(f"Technical Analysis: {symbol}Trend Detection", color = 'white', fontsize = 16)
    plt.legend()
    plt.grid(color = 'gray', linestyle = '--', alpha = 0.3)
    plt.show()

# run for anything on db
plot_expert_crossover("NEE")