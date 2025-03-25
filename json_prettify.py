#takes the card data file and spits it back out as pretty version
import json

CARD_FILE = 'cards/default-cards-20250325090811.json'
PRETTY_FILE = 'cards/pretty.json'

with open(CARD_FILE, 'r', encoding='utf-8') as file:
    data = json.load(file)

cards_text = json.dumps(data, indent=2)

with open(PRETTY_FILE, 'w', encoding='utf-8') as file:
    file.write(cards_text)


