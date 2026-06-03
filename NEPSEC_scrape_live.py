import requests
import pandas as pd

url = "https://nepseapi.surajrimal.dev/Summary"

# This 'headers' dictionary is your Passport
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    # Notice we added 'headers=headers' and 'timeout=10'
    response = requests.get(url, headers=headers, timeout=10)
    
    # Check if the server actually allowed us in (200 means OK)
    if response.status_code == 200:
        data = response.json()
        df = pd.Series(data).to_frame(name="Value")
        
        print("🔓 ACCESS GRANTED: LIVE NEPSE DATA")
        print("-" * 35)
        print(df)
        
        # Get a specific value like an Expert
        scrip_count = data.get('Total Scrips Traded:', 'N/A')
        print(f"\nCompanies Active Today: {scrip_count}")
    else:
        print(f"Server said No. Status Code: {response.status_code}")

except Exception as e:
    print(f"Final Defense Triggered: {e}")