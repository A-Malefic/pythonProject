import requests
from bs4 import BeautifulSoup
import json

url = "https://api.scryfall.com/cards/search?q=c%3Awhite+cmc%3D1"
#url = "https://api.scryfall.com/cards/search?q=c%21WB"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

response = requests.get(url, headers=headers)
js = json.loads(response.text)

list: object = (js['data'])

with open("js_wb.json", "w", encoding='utf-8') as file:
    json.dump(js, file, ensure_ascii=False, indent=4)

for data in list:
    print(data['name'],": ", data['type_line'], data['prices']['usd'], "usd")
    try:
        print(data['image_uris']['normal'])
    except KeyError:
        print("image uris")
        card_faces = data['card_faces']
        for card_fase in card_faces:
            print(card_faces['image_uris']['normal'])

#class Datacard