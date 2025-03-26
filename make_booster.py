#DOES NOT INCLUDE SPECIAL RARITY CARDS IDK WHAT THEY ARE

import json
import random
import os
from scryfall_api import make_default_cards_json

CARD_FILE = 'cards/default_cards.json'
rarity_List = ('common', 'uncommon', 'rare', 'mythic')

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
                if i['border_color'] != ('borderless'):
                    if i['nonfoil']:
                        if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                            cards.append(i['name'])
    return cards

#Get all uncommons in a set and return a list of them
def get_uncommon_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'uncommon':
                if i['border_color'] != ('borderless'):
                    if i['nonfoil']:
                        if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                            cards.append(i['name'])
    return cards

#Get all rares in a set and return a list of them
def get_rare_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'rare':
                if i['border_color'] != ('borderless'):
                    if i['nonfoil']:
                        if i['name'] not in ('Forest', 'Plains', 'Island', 'Mountain', 'Swamp'):
                            cards.append(i['name'])
    return cards

#Get all mythic rares in a set and return a list of them
def get_mythic_cards_in_set(set_code: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == 'mythic':
                if i['border_color'] != ('borderless'):
                    if i['nonfoil']:
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
def get_nonfoil_wildcards_in_set(set_code: str, rarity: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == rarity:
                if i['nonfoil']:
                    cards.append(i['name'])
    return cards

#Get all foil wildcards in a set and return a list of them
def get_foil_wildcards_in_set(set_code: str, rarity: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i ['rarity'] == rarity:
                if i['foil'] == True:
                    cards.append(i['name'])
    return cards

def make_play_booster(set_name: str):
    booster = []
    common_Sheet = make_Card_Sheet_Common(set_name)
    print(common_Sheet)
    common_Start_Card = random.choice(common_Sheet)
    common_Start_Index = common_Sheet.index(common_Start_Card)
    card_To_Add = 0
    loop_Common = 0

    #get commons
    for i in range(6):
        if card_To_Add + common_Start_Index <= len(common_Sheet) - 1 and loop_Common == 0:
            booster.append(common_Sheet[common_Start_Index + card_To_Add])
            print (common_Start_Index + i)
            print(card_To_Add)
            card_To_Add += 1
        else:
            loop_Common = 1
            card_To_Add = 0
            booster.append(common_Sheet[card_To_Add])
            card_To_Add += 1

    #get uncommons
    for i in range(3):
        card = random.choice(get_uncommon_cards_in_set(sets[set_name]))
        booster.append(card)

    #get rare/mythic rare
    rare_For_Pack = random.choices(rarity_List, weights = [0, 0, 87.5, 12.5])
    print(rare_For_Pack)
    if rare_For_Pack == ['rare']:
        booster.append(random.choice(get_rare_cards_in_set(sets[set_name])))
        print('ooh a rare')
    else:
        booster.append(random.choice(get_mythic_cards_in_set(sets[set_name])))
        print('ooh a mythic')

    #get land
    booster.append(random.choice(get_lands_in_set(sets[set_name])))

    #get non-foil wildcard
    rarity_For_Wild_NF = random.choices(rarity_List, weights = [33.3, 36.7, 17.5, 7.5])
    print(rarity_For_Wild_NF)
    booster.append(random.choice(get_nonfoil_wildcards_in_set(sets[set_name], rarity_For_Wild_NF[0])))


    #get foil wildcard
    rarity_For_Wild_F = random.choices(rarity_List, weights = [33.3, 36.7, 17.5, 7.5])
    booster.append(random.choice(get_foil_wildcards_in_set(sets[set_name], rarity_For_Wild_F[0])))
    print(rarity_For_Wild_F)

    return booster

#makes a sheet of common cards
def make_Card_Sheet_Common(set_Name: str):
    sheet = get_common_cards_in_set(sets[set_Name])
    sheet_Length = len(sheet)
    rows = find_Greatest_Common_Factor(sheet_Length)
    columns = sheet_Length//rows
    collation = collation_Sim(rows,columns,sheet)
    return collation

#finds the greatest common factor of a number up to 16
def find_Greatest_Common_Factor(length: int):
    greatest_Common_Factor = 0
    for i in range(16):
        if i > 0:
            if length % i == 0 and  i != 1 and i != length and i > greatest_Common_Factor and length/i <= i:
                greatest_Common_Factor = i
    return greatest_Common_Factor

#Simulates the manufacturing process of cards
def collation_Sim(rows: int, columns: int,sheet):
    sheet_Length = len(sheet) - 1
    collation = []
    rows_Per_Column = random.randint(3, 5)
    row_To_Stop = rows_Per_Column
    current_Row = 0
    while current_Row <= rows - 1:
        current_Column = 0
        while current_Column <= columns - 1:
            for i in range(row_To_Stop - current_Row):
                collation.append(sheet[sheet_Length - (((current_Row + 1) * (columns)) + current_Column + 1)])
                current_Row += 1
            current_Column += 1
            current_Row = row_To_Stop - rows_Per_Column
        current_Row = row_To_Stop
        rows_Per_Column = random.randint(3, 5)
        row_To_Stop = row_To_Stop + rows_Per_Column
        if row_To_Stop > rows:
            rows_Per_Column = rows - (row_To_Stop - rows_Per_Column)
            row_To_Stop = rows

    return collation


#Examples
#print(sets)
print(make_play_booster('Aetherdrift'))
#print(get_cards_in_set('war'))
#print(get_cards_in_set(sets['Guilds of Ravnica']))
#print(make_Card_Sheet_Common('Aetherdrift'))

