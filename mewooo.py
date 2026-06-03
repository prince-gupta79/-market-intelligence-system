import requests

TOKEN = "8724582515:AAEElkYDy06wM70CR9m9dASomqENsgmZfuY"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print("Calling url:",  url)
response = requests.get(url)
print(response.text)