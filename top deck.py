import requests
from bs4 import BeautifulSoup
import json


url = "https://topdeck.ru/apps/toptrade/auctions"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

response = requests.get(url, headers=headers)
raw = response.text


with open("js_topdeck.json", "w", encoding='cp1251') as file:
    json.dump(raw, file, ensure_ascii=False, indent=4)

with open("file.html", "w", encoding='cp1251') as file:
    file.write(raw)

#with open('js_topdeck.json', encoding='cp1251') as file:
#    data = json.load(file)


print(json.dumps(raw))