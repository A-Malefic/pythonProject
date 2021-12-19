import requests
import json

url = "https://topdeck.ru/apps/toptrade/api-v1/auctions"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}

response = requests.get(url, headers=headers)
js = json.loads(response.text)

with open("js_topdeck.json", "w", encoding='utf-8') as file:
    json.dump(js, file, ensure_ascii=False, indent=4)

with open("js_topdeck.json", encoding='utf-8') as file:
    json = json.load(file)

for lot in json:
    print(lot['lot'], 'Цена', lot['current_bid'], 'Локация', lot['shipping_info_quick'], 'Условия доставки', lot['shipping_info'], 'Изображение', lot['image_url'])
    #print(lot)

