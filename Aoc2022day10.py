#consider the signal strength (the cycle number multiplied by the value of the X register) 
# during the 20th cycle and every 40 cycles after that (that is, during the 20th, 60th, 100th, 140th, 180th, and 220th cycles).

lines = open('test.txt').read().splitlines()

register = 1
cycles = [1,1]
for line in lines:
    if line.startswith("add"):
        cycles.append(register)
        register += int(line.split()[1]) 
        cycles.append(register)
    else:
        cycles.append(register)
#print(cycles)

#print(cycles[180])

def get_strengths(lists, start, step):
    strengths = 0
    for i in range(start, len(lists), step):
        strengths += i * lists[i]
    return strengths

#strength = get_strengths(cycles, 20, 40)
#print(strength)
def screen(cycles):
    row = ''
    for i in range(40):
        if i in [cycles[i] -1, cycles[i], cycles[i]+1]:
            row += '#'
        else:
            row += '.'
    return row
row1 = screen(cycles[1:41])
print(row1)
row2 = screen(cycles[41:81])
print(row2)
row3 = screen(cycles[81:121])
print(row3)
row4 = screen(cycles[121:161])
print(row4)
row5 = screen(cycles[161:201])
print(row5)
row6 = screen(cycles[201:241])
print(row6)