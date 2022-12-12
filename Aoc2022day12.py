class Elevation:
    def __init__(self, row, col, parent):
        self.row = row
        self.col = col
        self.parent = parent

def isValid(row, col, data, visited):
    if (row >= 0 and col >= 0 and row < len(data) 
    and col < len(data[0]) and visited[row][col]==0):
        return True
    return False 

def isSafe(row1,col1,row2,col2,data):
    if (ord(data[row1][col1]) - ord(data[row2][col2]) == 1 
    or ord(data[row1][col1]) == ord(data[row2][col2])
    or ord(data[row1][col1]) - ord(data[row2][col2]) == -53
    or ord(data[row1][col1]) - ord(data[row2][col2]) == -52
    or ord(data[row1][col1]) < ord(data[row2][col2])):
        return True
    return False

def BFS(data, start) -> Elevation:
    visited = [[0 for i in range(len(data[0]))] for j in range(len(data))]
    visited[start.row][start.col] = 1
    queue = []
    queue.append(start)

    while len(queue)>0:
        start = queue.pop(0)
        # reach destination
        if (data[start.row][start.col] == 'E'):
            return start
        # move down
        if (isValid(start.row + 1, start.col, data, visited) 
        and isSafe(start.row + 1, start.col, start.row, start.col, data)):
            queue.append(Elevation(start.row + 1, start.col, start))
            visited[start.row + 1][start.col] = 1
        # move right
        if (isValid(start.row,  start.col + 1, data, visited) 
        and isSafe(start.row, start.col + 1, start.row, start.col, data)):
            queue.append(Elevation(start.row, start.col + 1, start))
            visited[start.row][start.col + 1] = 1
        # move up
        if (isValid(start.row - 1, start.col, data, visited) 
        and isSafe(start.row - 1, start.col, start.row, start.col, data)):
            queue.append(Elevation(start.row - 1, start.col, start))
            visited[start.row - 1][start.col] = 1
        # move left
        if (isValid(start.row, start.col - 1, data, visited) 
        and isSafe(start.row, start.col - 1, start.row, start.col, data)):
            queue.append(Elevation(start.row, start.col - 1, start))
            visited[start.row][start.col - 1] = 1

lines = open('test.txt').read().splitlines()
data = [[*line] for line in lines]

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            data[i][j] = 'a'
            node = BFS(data, Elevation(i,j,None))
            break

distance = 0
while(node.parent != None):
    node = node.parent
    distance += 1

print(distance)

# Part 2:
distances = []
shortestPath = [[0 for i in range(len(data[0]))] for j in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 'S':
            data[i][j] = 'a'
        if data[i][j] == 'a':
            try:
                node = BFS(data, Elevation(i,j,None))
                distance = 0
                while(node.parent != None):
                    node = node.parent
                    distance += 1
                distances.append(distance)
            except:
                pass

print(min(distances))