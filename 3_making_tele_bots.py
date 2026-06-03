import requests

def send_telegram_msg(message):
    # my configurations
    TOKEN = "8724582515:AAEElkYDy06wM70CR9m9dASomqENsgmZfuY" # replace with your bot token
    CHAT_ID = "7965377966" # replace with your chat id

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"}  # this will allows for bold of italic texting style'''
    

    try :
        response = requests.post(url, data = payload)
        if response.status_code == 200:
            print("ALERT sent to your phone")
        else:
            print(f"FAILED TO SEND alert: {response.text}")

    except Exception as e:
        print(f"Telegram Error: {e}")

# adding a tesx msg
send_telegram_msg("mummy ")