#DOES NOT INCLUDE SPECIAL RARITY CARDS IDK WHAT THEY ARE

import json
import random
import os
from scryfall_api import make_default_cards_json

CARD_FILE = 'cards/default_cards.json'
if not os.path.exists(CARD_FILE):
    print('Missing Card File, downloading from scryfall...')
    make_default_cards_json()

with open(CARD_FILE, 'r', encoding='utf-8') as file:
    jdata = json.load(file)

#Get Full set code list and delete copies
set_code_list = []

for i in jdata:
    set_code_list.append(i['set'])

set_code_list = list(set(set_code_list))
set_code_list.sort()
#print(f"Number of unique sets: {len(setcodelist)}")


#Get Full set name list and delete copies
set_name_list = []
for i in jdata:
    set_name_list.append(i['set_name'])
set_name_list = list(set(set_name_list))
set_name_list.sort()
#print(f"Number of unique set names: {len(setNames)}")


#Function to get set names and associated set codes
def get_set_dict():
    setDict = {}

    for i in set_name_list:
        for j in jdata:
            if i == j['set_name']:
                setDict[i] = j['set']
                break

    return setDict

#Call and print the set code for a given set name
sets = get_set_dict()
#print(sets['Time Spiral'])

#Get all cards in a set and return a list of them
def get_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            cards.append(i['name'])
    return cards

'''
timespiral_cards = get_cards_in_set(sets['Time Spiral'])
print(timespiral_cards)
print(len(timespiral_cards))
'''

#Get all commons in a set and return a list of them
def get_common_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'common':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i['name'])
    return cards

#Get all uncommons in a set and return a list of them
def get_uncommon_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'uncommon':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i['name'])
    return cards

#Get all rares in a set and return a list of them
def get_rare_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'rare':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i['name'])
    return cards

#Get all mythic rares in a set and return a list of them
def get_mythic_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'mythic':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i['name'])
    return cards

#Get all lands in a set and return a list of them
def get_lands_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['type_line'] in ('Basic Land — Forest', 'Basic Land — Plains', 'Basic Land — Island', 'Basic Land — Mountain', 'Basic Land — Swamp'):
                cards.append(i['name'])
    return cards

#Get all non-foil wildcards in a set and return a list of them
def get_nonfoil_wildcards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['nonfoil']:
                cards.append(i['name'])
    return cards

#Get all foil wildcards in a set and return a list of them
def get_foil_wildcards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['foil'] == True:
                cards.append(i['name'])
    return cards

def make_play_booster(set_name: str):
    booster = []

    #get commons
    for i in range(7):
        card = random.choice(get_common_cards_in_set(sets[set_name]))
        booster.append(card)

    #get uncommons
    for i in range(3):
        card = random.choice(get_uncommon_cards_in_set(sets[set_name]))
        booster.append(card)

    #get rare/mythic rare

    for i in range(2):
        if random.randint(0, 1) == 0:
            booster.append(random.choice(get_rare_cards_in_set(sets[set_name])))
        else:
            booster.append(random.choice(get_mythic_cards_in_set(sets[set_name])))

    #get land
    booster.append(random.choice(get_lands_in_set(sets[set_name])))

    #get non-foil wildcard
    booster.append(random.choice(get_nonfoil_wildcards_in_set(sets[set_name])))

    #get foil wildcard
    booster.append(random.choice(get_foil_wildcards_in_set(sets[set_name])))

    return booster

#Examples
print(sets)
print(make_play_booster('Aetherdrift'))
print(get_cards_in_set('war'))
print(get_cards_in_set(sets['Guilds of Ravnica']))

