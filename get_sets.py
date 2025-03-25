#All this does is take the json and make a nice pretty dictionary that has all the set names('set-name') and their associated setcodes('set')

import json

with open('cards/default-cards-20250325090811.json', 'r', encoding='utf-8') as file:
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


sets = get_set_dict()
print(sets['Time Spiral'])
