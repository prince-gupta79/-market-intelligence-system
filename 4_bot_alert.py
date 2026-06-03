import yfinance as yf
import requests

def send_telegram_msg(message):
    TOKEN = "8724582515:AAEElkYDy06wM70CR9m9dASomqENsgmZfuY" # replace with your bot token
    CHAT_ID = "7965377966" # replace with your chat id

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"}  # this will allows for bold of italic texting style'''
    requests.post(url, data = payload)

def monitor_with_alerts():
    target = 175.00
    symbol = "NVDA"

    ticker = yf.Ticker(symbol)
   
    # fetching
    price = ticker.fast_info['last_price']

    # checking validation
    # instead of dropna, we check if the data is "same"
    if price is None or price <= 0:
        print("Data ERROR detected. Skipping this route...")
        return # exit the function for this round
    
    print(f"Tracking {symbol}: ${price:.2f}")

    if price >= target:
        alert_text = f"MUJI!! profit voo \nAsset: {symbol} \nPrice: ${price:.2f}"
        send_telegram_msg(alert_text)
        return True 
    return False
monitor_with_alerts()