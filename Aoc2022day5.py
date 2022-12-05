all_lines = open('test.txt').read().splitlines()
breakpoint =  all_lines.index('')

supplies = all_lines[:breakpoint-1]

num_stacks = len(supplies[0])//3

cleansupplies = []
for line in supplies:
    for i in range(num_stacks):
        cleansupplies.append(line[4*i+1::12])

stacks = [[]]*num_stacks
for i in range(num_stacks):
    stacks[i] = cleansupplies[i::3][::-1]
    stacks[i] = ' '.join(stacks[i]).split()
print(stacks)

procedures = all_lines[breakpoint+1:]

def CrateMover9000(q, f ,t):
    for i in range(q):
        t.append(f.pop())
    return f,t

def CrateMover9001(q, f ,t):
    temp = []
    new_f = []
    if (q<len(f)):
        temp = f[-q:]
        new_f = f[:-q]
    else:
        temp = f
    for i in temp:
        t.append(i)
    return new_f,t

for step in procedures:
    info = step.split(' ')
    stacks[int(info[3])-1], stacks[int(info[5])-1] = CrateMover9001(int(info[1]), stacks[int(info[3])-1], stacks[int(info[5])-1])

crates=''
for i in stacks:
    crates += i[-1]
print(crates)