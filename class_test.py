import requests
import json

class Datacard():
    response = requests.get("https://api.scryfall.com/cards/search?q=c%21WB")

    def __init__(self):
        print("init")

    def get_data(self):
        self.cardslist = json.loads(Datacard.response.text)

    def card_price(self):
        for data in self.cardslist['data']:
            self.name = data.get('name')
            self.type_line = data.get('type_line')
            self.price = data.get('prices').get('usd')
            self.image = data.get('image_uris', {}).get('normal')
            self.card_image = data.get('card_faces')
            print(self.name, self.type_line, self.price, self.image)
            if self.image is None:
                for card in self.card_image:
                    print(card['image_uris']['normal'])

    def save_json(self):
        with open("js_class.json", "w", encoding='utf-8') as file:
            json.dump(self.cardslist, file, ensure_ascii=False, indent=4)

d = Datacard()
d.get_data()
d.card_price()
#d.save_json()
