import json
import random
import os
from pathlib import Path
from datetime import datetime
from typing import Any

from scryfall_api import make_default_cards_json

#Check if the cards folder exists, if not create it
Path("cards").mkdir(parents=True, exist_ok=True)

#Check if card file exists, if not download it
CARD_FILE = 'cards/default_cards.json'
if not os.path.exists(CARD_FILE):
    print('Missing Card File, downloading from scryfall...')

    make_default_cards_json()

with open(CARD_FILE, 'r', encoding='utf-8') as file:
    jdata = json.load(file)

#Checks if boosters folder exists, if not create it
Path("boosters").mkdir(parents=True, exist_ok=True)

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

#Function for making a lowercase dictionary for use in Clayton booster to be case insensitive
def lowercase_keys(input_dict):
    return {key.lower(): value for key, value in input_dict.items()}

#Call and print the set code for a given set name
sets = get_set_dict()

#create a lowercase set dictionary for Clayton booster function
lower_sets = lowercase_keys(sets)


#Get all cards in a set and return a list of the card objects
def get_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            cards.append(i)
    return cards

#Get all commons in a set and return a list of them
def get_common_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'common':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i)
    return cards

#Get all uncommons in a set and return a list of them
def get_uncommon_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'uncommon':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i)
    return cards

#Get all rares in a set and return a list of them
def get_rare_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'rare':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i)
    return cards

#Get all mythic rares in a set and return a list of them
def get_mythic_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'mythic':
                if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                    cards.append(i)
    return cards

#Get all lands in a set and return a list of them
def get_lands_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['type_line'] in ('Basic Land — Forest', 'Basic Land — Plains', 'Basic Land — Island', 'Basic Land — Mountain', 'Basic Land — Swamp'):
                cards.append(i)
    return cards

#Get all non-foil wildcards in a set and return a list of them
def get_nonfoil_wildcards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['nonfoil']:
                cards.append(i)
    return cards

#Get all foil wildcards in a set and return a list of them
def get_foil_wildcards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['foil'] == True:
                cards.append(i)
    return cards

#makes a booster pack and returns a list of the card objects
def make_play_booster(set_code: str):
    booster = []

    #get commons
    for i in range(7):
        card = random.choice(get_common_cards_in_set(set_code))
        booster.append(card)

    #get uncommons
    for i in range(3):
        card = random.choice(get_uncommon_cards_in_set(set_code))
        booster.append(card)

    #get rare/mythic rare

    for i in range(2):
        if random.randint(0, 1) == 0:
            booster.append(random.choice(get_rare_cards_in_set(set_code)))
        else:
            booster.append(random.choice(get_mythic_cards_in_set(set_code)))

    #get land
    booster.append(random.choice(get_lands_in_set(set_code)))

    #get non-foil wildcard
    booster.append(random.choice(get_nonfoil_wildcards_in_set(set_code)))

    #get foil wildcard
    booster.append(random.choice(get_foil_wildcards_in_set(set_code)))

    #this is where the token would be added, but i didnt do that

    return booster

#Creates a booster pack and saves it to a json file
def export_play_booster(set_name: str):
    #Makes the booster pack
    booster = make_play_booster(set_name)

    #Creates a unique filename, so you don't overwrite any boosters you've made
    time_now = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    JSON_NAME = f"boosters/{set_name} Booster {time_now}.json"

    #Saves the booster pack to a json file
    with open(JSON_NAME, 'w', encoding='utf-8') as file:
        #json.dump([card for card in booster], file, indent=4, ensure_ascii=False)
        json.dump(booster, file)

    print(f'Exported Booster Pack to {JSON_NAME}')

#Example of exporting booster
#export_play_booster('Aetherdrift')


#The Clayton booster function, uses lower_sets and casefold to be case insensitive
def make_clayton_booster(set_name: str, booster_type: str) -> list[dict] | None:
    if set_name.casefold() not in lower_sets.keys():
        print('Not a valid set, please try again')
    else:
        print('wow its a set')
        match booster_type.casefold():
            case 'play':
                return make_play_booster(lower_sets[set_name.casefold()])

        print('Not a valid booster type, please try again')
        return None



#Examples of input checking
print(make_clayton_booster('aetherdrift','play'))
print(make_clayton_booster('aeTHerdrIft','play'))
print(make_clayton_booster('aeTH erdrIft','play'))
print(make_clayton_booster('aeTHerdrIft','commander'))