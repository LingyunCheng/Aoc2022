from itertools import groupby
import json

lines = open('test.txt').read().splitlines()
pairs = [list(sub) for ele, sub in groupby(lines, key=bool) if ele]
#print(pairs)

def compare(left, right):
    len_left = len(left)
    len_right = len(right)
    if len_left==0:
        return True
    elif len_right==0:
        return False
    else:
        for i in range(len_left):
            if i > len_right-1:
                return False
            elif left[i] == right[i] and i<len_left-1:
                continue
            elif left[i] == right[i] and i==len_left-1 and i<len_right-1:
                return True
            elif isinstance(left[i],int) and isinstance(right[i],int):
                if left[i] < right[i]:
                    return True
                elif left[i] > right[i]:
                    return False
                else:
                    continue
            elif isinstance(left[i],list) and isinstance(right[i],int):
                return compare(left[i],[right[i]])
            elif isinstance(left[i],int) and isinstance(right[i],list):
                return compare([left[i]],right[i])
            elif isinstance(left[i],list) and isinstance(right[i],list):
                return compare(left[i],right[i])

total = 0
for i in range(len(pairs)):
    res = compare(json.loads(pairs[i][0]), json.loads(pairs[i][1]))
    if res is True:
        total += i+1
print(total)

# part 2
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if compare(json.loads(array[j]), json.loads(pivot)):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
  
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

data = ' '.join(lines).split()
data.append('[[2]]')
data.append('[[6]]')
quick_sort(data, 0, len(data) - 1)
res = (data.index('[[2]]') + 1)*(data.index('[[6]]')+1)
print(res)
