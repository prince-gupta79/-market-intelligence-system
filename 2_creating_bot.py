# In this we are gonna makaing a bot to signal us if the certain 
# conditions are met in the live data (sentinel script)
import yfinance as yf
import time

# EXPERT CONFIGURATION
TARGET_PRICE = 180.00  # Seting  target for NVIDIA
SYMBOL = "NVDA"

def monitor_market():
    print(f"📡 Sentinel Active: Monitoring {SYMBOL} for Target ${TARGET_PRICE}...")
    
    while True:
        try:
            ticker = yf.Ticker(SYMBOL)
            # Fetching the last price
            current_price = ticker.fast_info['last_price']
            
            if current_price >= TARGET_PRICE:
                print(f"🚨 ALERT! {SYMBOL} has hit ${current_price:.2f}!")
                print("ACTION: Execute Trade or Notify Management.")
                # In a real job, this is where you'd trigger an Email or Telegram message
                break 
            else:
                print(f"Status: {SYMBOL} is at ${current_price:.2f}. Standing by...")
            
            # Wait 60 seconds before checking again (Standard API etiquette)
            time.sleep(60) 
            
        except Exception as e:
            print(f"⚠️ Connection glitch: {e}")
            time.sleep(10)

monitor_market()