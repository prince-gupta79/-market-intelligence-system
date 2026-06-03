import feedparser
from textblob import TextBlob
import urllib.request

def check_internet():
    try:
        urllib.request.urlopen("http://www.google.com",timeout=5)
        return True
    except:
        return False

def get_market_sentiment(asset_name):
    # using a standrad Financial RSS feed [yahoo finance]
    url = f"https://news.google.com/rss/search?q={asset_name}+stock&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)

    print(f" --- LIVE INTELLEGENT: {asset_name} ---")

    total_sentiment = 0
    count = 0

    for entry in feed.entries[:5]: # lets look at the 5 most recent news item
        analysis = TextBlob(entry.title)
        score = analysis.sentiment.polarity
        total_sentiment += score
        count += 1

        print(f"{entry.title}")
        print(f"score : {score:.2f}")
    if count == 0:
        print("no news found..")
        return

    avg_sentiment = total_sentiment / count
    print(f"\n OVERALL WORLD SENTIMENT: {avg_sentiment:.2f}")

    if avg_sentiment > 0.1:
        print("MARKET MOOD: optimistic")
    elif avg_sentiment < -0.1:
        print("MARKET MOOD: fearful")
    else:
        print("MARKET MOOD: uncertain")

# for gold
get_market_sentiment("GLD")
