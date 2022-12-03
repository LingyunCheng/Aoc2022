from enum import Enum

def priority_letter(letter):
    if (letter.isupper()):
        priority = ord(item)-38
    elif (letter.islower()):
        priority = ord(item)-96
    else:
        priority = 0
    return priority
    

data = open("day3data.txt").read().splitlines()

# part one
bags = [list(set(bag[:(len(bag)//2)])& set(bag[(len(bag)//2):])) for bag in data]

priotities = 0
for items in bags:
    for item in items:
        priotities += priority_letter(item)
        
print(priotities)

# part two
groups = [data[i:i+3] for i in range(0,len(data),3)]
badge = [list(set(group[0]) & set(group[1]) & set(group[1])) for group in groups]

priotities = 0
for items in badges:
    for item in items:
        priotities += priority_letter(item)
print(priotities)