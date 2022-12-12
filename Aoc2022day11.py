from itertools import groupby
import re

lines = open('test.txt').read().splitlines()
# remove blank lines
lines = [list(sub) for ele, sub in groupby(lines, key = bool) if ele]
#print(lines)

monkeys = []
for i in range (len(lines)):
    start = [ int(x) for x in re.findall(r'-?\d+\.?\d*', lines[i][1])] 
    monkeys.append(start)
#print(monkeys)

def each_turn(m_from,old):
    if m_from == 0:
        new = old * 7
        current = new % 9699690
        if current % 11 == 0:
            m_to = 2
        else:
            m_to = 6
    elif m_from == 1:
        new = old * 13
        current = new % 9699690
        if current % 5 == 0:
            m_to = 7
        else:
            m_to =4
    elif m_from == 2:
        new = old + 1
        current = new % 9699690
        if current % 7 == 0:
            m_to = 1
        else:
            m_to = 7
    elif m_from == 3:
        new = old * old
        current = new % 9699690
        if current % 2 == 0:
            m_to = 0
        else:
            m_to = 6
    elif m_from == 4:
        new = old + 7
        current = new % 9699690
        if current % 17== 0:
            m_to = 3
        else:
            m_to = 5
    elif m_from == 5:
        new = old + 6
        current = new % 9699690
        if current % 13 == 0:
            m_to = 3
        else:
            m_to = 0
    elif m_from == 6:
        new = old + 4
        current = new % 9699690
        if current % 3== 0:
            m_to = 1
        else:
            m_to = 2
    else:
        new = old + 8
        current = new % 9699690
        if current % 19 == 0:
            m_to = 4
        else:
            m_to = 5
    return current, m_to

def test_turn(m_from,old,value):
    if m_from == 0:
        new = old * 19
        current = new % value
        if current % 23 == 0:
            m_to = 2
        else:
            m_to = 3
    elif m_from == 1:
        new = old + 6
        current = new % value
        if current % 19 == 0:
            m_to = 2
        else:
            m_to = 0
    elif m_from == 2:
        new = old * old
        current = new % value
        if current % 13 == 0:
            m_to = 1
        else:
            m_to = 3
    else:
        new = old + 3
        current = new % value
        if current % 17 == 0:
            m_to = 0
        else:
            m_to = 1
    return current, m_to


def each_round(monkeys, numofmonkeys):
    new_monkeys = [[] for k in range(numofmonkeys)]
    times = [0 for m in range(numofmonkeys)] 
    for i in range(numofmonkeys):
        # if this monkey holds some items
        lists = monkeys[i]+new_monkeys[i]
        times[i] = len(monkeys[i])+ len(new_monkeys[i])
        if lists:
            for item in lists:
                new_item, m_to = each_turn(i, item)
                #print("new item:"+str(new_item))
                new_monkeys[m_to].append(new_item)
                if item in new_monkeys[i]:
                    new_monkeys[i].remove(item)
                #print(new_monkeys)
    #new_monkeys[-1] = []
    return new_monkeys,times

round = 10000
numofmonkeys = 8
times = [0 for i in range(numofmonkeys)] 
for i in range(round):
    monkeys, time = each_round(monkeys,numofmonkeys)
    for j in range(numofmonkeys):
        times[j] += time[j]
    #print(monkeys)


print(times)



