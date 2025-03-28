#DOES NOT INCLUDE SPECIAL RARITY CARDS IDK WHAT THEY ARE

import json
import random
import os
from scryfall_api import make_default_cards_json

CARD_FILE = 'cards/default_cards.json'
rarity_List = ('common', 'uncommon', 'rare', 'mythic')
slot_Seven = ['common', 'list']
list_Rarity = ['common','uncommon', 'rare', 'mythic', 'Special Guests']

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
            cards.append(i)
    return cards

'''
timespiral_cards = get_cards_in_set(sets['Time Spiral'])
print(timespiral_cards)
print(len(timespiral_cards))
'''

#Get all commons in a set and return a list of them
def get_rarity_cards_in_set(set_code: str, rarity: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == rarity:
                if i['border_color'] != ('borderless'):
                    if i['nonfoil']:
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
def get_nonfoil_wildcards_in_set(set_code: str, rarity: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == rarity:
                if i['nonfoil']:
                    cards.append(i)
    return cards

#Get all foil wildcards in a set and return a list of them
def get_foil_wildcards_in_set(set_code: str, rarity: str) -> list:
    cards = []
    for i in jdata:
        if i['set'] == set_code:
            if i['rarity'] == rarity:
                if i['foil'] == True:
                    cards.append(i)
    return cards

def get_List_Card(set_code: str):
    cards = []
    rarity = random.choices(list_Rarity, weights = [37.52, 37.52, 6.24, 6.24, 12.48])
    print(rarity)
    for i in jdata:
        if rarity != ['Special Guests']:
            if i['set'] == ['The List']:
                print('not a guest')
                if i['rarity'] == rarity:
                    cards.append(i)
    return cards



def make_play_booster(set_code: str):
    booster = []
    common_Sheet = make_Card_Sheet_Common(set_code)
    print(common_Sheet)
    common_Start_Card = random.choice(common_Sheet)
    common_Start_Index = common_Sheet.index(common_Start_Card)
    card_To_Add = 0

    #get commons
    for i in range(7):
        if i != 6:
            if card_To_Add + common_Start_Index <= len(common_Sheet) - 1:
                booster.append(common_Sheet[common_Start_Index + card_To_Add])
                card_To_Add += 1
            else:
                common_Start_Index = 0
                card_To_Add = 0
                booster.append(common_Sheet[common_Start_Index])
                card_To_Add += 1
        else:
            card_Seven = random.choices(slot_Seven, weights = [87.5, 12.5])
            if card_Seven == ['common']:
                if card_To_Add + common_Start_Index <= len(common_Sheet) - 1:
                    booster.append(common_Sheet[common_Start_Index + card_To_Add])
                else:
                    common_Start_Index = 0
                    booster.append(common_Sheet[common_Start_Index])
            else:
                get_List_Card(set_code)



    #get uncommons
    for i in range(3):
        card = random.choice(get_rarity_cards_in_set(set_code, 'uncommon'))
        booster.append(card)

    #get rare/mythic rare
    rare_For_Pack = random.choices(rarity_List, weights = [0, 0, 87.5, 12.5])
    if rare_For_Pack == ['rare']:
        booster.append(random.choice(get_rarity_cards_in_set(set_code, 'rare')))
    else:
        booster.append(random.choice(get_rarity_cards_in_set(set_code, 'mythic')))

    #get land
    booster.append(random.choice(get_lands_in_set(set_code)))

    #get non-foil wildcard
    rarity_For_Wild_NF = random.choices(rarity_List, weights = [33.3, 36.7, 17.5, 7.5])
    booster.append(random.choice(get_nonfoil_wildcards_in_set(set_code, rarity_For_Wild_NF[0])))


    #get foil wildcard
    rarity_For_Wild_F = random.choices(rarity_List, weights = [33.3, 36.7, 17.5, 7.5])
    booster.append(random.choice(get_foil_wildcards_in_set(set_code, rarity_For_Wild_F[0])))

    return booster


#makes a sheet of common cards
def make_Card_Sheet_Common(set_code: str):
    sheet = get_rarity_cards_in_set(set_code, 'common')
    sheet_Length = len(sheet)
    columns = factoring_Easy_Peasy(sheet_Length)
    rows = sheet_Length//columns
    collation = collation_Sim(rows,columns,sheet)
    return collation


#find the factors with the smallest difference
def factoring_Easy_Peasy(length: int):
    factors= []
    differences = []
    factor_To_Send: int
    for i in range(length):
        if i not in [0,1,length]:
            if length % i == 0 and length/i not in factors:
                factors.append(i)
    for i in range (len(factors)):
        differences.append(length // factors[i])
    index_For_Factor = differences.index(min(differences))
    factor_To_Send = factors[index_For_Factor]
    return factor_To_Send


#Simulates the manufacturing process of cards
#pretends the cards are placed in a grid and takes the first card in the last row and stacks
#the card above it on top, and does this from 3-5 times before moving to the next column,
#then it stacks those piles where the left is the bottom and the right is the top,
#the process then repeats until all the rows have been stacked
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
#print(make_play_booster('dft'))
b = make_play_booster('dft')
with open('test.json', 'w') as outfile:
    json.dump(b, outfile, indent=4)
#print(get_cards_in_set('war'))
#print(get_cards_in_set(sets['Guilds of Ravnica']))
#print(make_Card_Sheet_Common('Aetherdrift'))

print(len(b))