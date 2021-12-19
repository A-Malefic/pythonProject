import requests
import json

class Current_aucs():
    response = requests.get("https://topdeck.ru/apps/toptrade/api-v1/auctions")

    def __init__(self):
        print("init")

    def get_caucs(self):
        self.caucs = json.loads(Current_aucs.response.text)

    def save_json_caucs(self):
        with open("js_current_auctions.json", "w", encoding='utf-8') as file:
            json.dump(self.caucs, file, ensure_ascii=False, indent=4)

    def print_caucs(self):
        with open("js_current_auctions.json", encoding='utf-8') as file:
            json_caucs = json.load(file)

        for lot in json_caucs:
            print(lot['lot'], 'Цена', lot['current_bid'], 'Локация', lot['shipping_info_quick'], 'Условия доставки',
                  lot['shipping_info'], 'Изображение', lot['image_url'])

class Single_card():
    response = requests.get("https://topdeck.ru/apps/toptrade/api-v1/singles/search?q=Dark+Ritual")

    def __init__(self):
        print("init")

    def get_single_card(self):
        self.single_card = json.loads(Single_card.response.text)

    def save_single(self):
        with open("js_single_card.json", "w", encoding='utf-8') as file:
            json.dump(self.single_card, file, ensure_ascii=False, indent=4)

    def print_single(self):
        with open("js_single_card.json", encoding='utf-8') as file:
            json_single = json.load(file)
            for name in json_single:
                print(name['name'], 'Цена', name['cost'], 'руб', 'Изображение', name['url'])

a = Current_aucs()
s = Single_card()
#a.get_caucs()
#a.save_json_caucs()
#a.print_caucs()
#s.get_single_card()
#s.save_single()
s.print_single()