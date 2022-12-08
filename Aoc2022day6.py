with open('data.txt', 'r') as file:
    buffer = file.read().replace('\n', '')

marker = []
res = 0
for i in range(14, len(buffer)):
    marker = buffer[i-14:i]
    repeat = False
    for j in marker:
        if marker.count(j) > 1:
            repeat = True
    if not repeat:
        print(i)
        break