from itertools import groupby

all_lines = open('day1test.txt').read().splitlines()

# remove blank lines
lines = [list(sub) for ele, sub in groupby(lines, key = bool) if ele]

# sum the carried calories for each elf
total_cal = []
for line in lines:
    # cast the element in list from string to int
    int_line = list(map(int,line))
    each_elf = sum(int_line)
    total_cal.append(each_elf)
    
# find the max value
max_cal = max(total_cal)
max_elf = total_cal.index(max_cal)

# find the 3 highest value
total_cal.sort()
top3 = total_cal[-3]