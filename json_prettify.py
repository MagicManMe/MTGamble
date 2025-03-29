#takes the card data file and spits it back out as pretty version
import json

CARD_FILE = 'cards/default_cards.json'
PRETTY_FILE = 'cards/pretty.json'


if __name__ == '__main__':
    with open(CARD_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)

    cards_text = json.dumps(data, indent=2)

    with open(PRETTY_FILE, 'w', encoding='utf-8') as file:
        file.write(cards_text)

