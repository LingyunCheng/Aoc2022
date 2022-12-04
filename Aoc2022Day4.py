all_camps = open("day3data.txt").read().splitlines()

# part one
counter = 0
for camp in all_camps:
    pair = camp.split(',')
    left_elf = pair[0].split('-')
    right_elf = pair[1].split('-')
    left = int(left_elf[0])-int(right_elf[0])
    right = int(left_elf[1])-int(right_elf[1])
    if (left * right <=0 ):
        counter += 1
    
print(counter)  

# part two
counter = 0
for camp in all_camps:
    pair = camp.split(',')
    left_elf = pair[0].split('-')
    right_elf = pair[1].split('-')
    both_left = int(left_elf[0])-int(right_elf[0])
    both_right = int(left_elf[1])-int(right_elf[1])
    left_right = int(left_elf[0])-int(right_elf[1])
    right_left = int(left_elf[1])-int(right_elf[0])
    if (both_left * right_left <= 0 or left_right * both_right <=0 or both_left * both_right <=0):
        counter += 1
    
print(counter)  