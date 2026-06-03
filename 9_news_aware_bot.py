from textblob import TextBlob

# sample news
headlines = [
    "Gold prices soar as global uncertanity grows.\n"
    "Investors dump gold as interest rates rises unexpecetedly.\n"
    "New gold mine discovery in Nepal boosts local economy.\n"
    ]

print("--- SENTIMENT ANALYSIS REPORT ---")

for news in headlines:
    analysis = TextBlob(news)
    # polarity: -1 (very -ve) & +1 (very +ve)
    sentiment = analysis.sentiment.polarity

    status = "POSITIVE" if sentiment > 0 else "NEGATIVE" if sentiment< 0 else "NETURAL"

    print(f"News:{news}")
    print(f"score:{sentiment:.2f} --- Result: {status}\n")