from enum import Enum

class opponent(Enum):
    A = 1
    B = 2
    C = 3 
    
class player(Enum):
    X = 1
    Y = 2
    Z = 3
    
class result(Enum):
    X = 0
    Y = 3
    Z = 6   
    
def hand_score(p1, p2):
    if (p2 - p1) == 0:
        score = 3
    elif (p2 -p1) == 1 or (p2 -p1) == -2:
        score = 6
    else:
        score = 0
    return score

def hand_shape(p1, end):
    if end == 0:
        p2 = (p1 -1) if p1 > 1 else 3
    elif end == 3:
        p2 = p1
    else:
        p2 = (p1 + 1) if p1 <3 else 1
    return p2

data = open("day2data.txt").read().splitlines()
rounds = [list(sub.split()) for sub in data]

# part one
guess_total = 0