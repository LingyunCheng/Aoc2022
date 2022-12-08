class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        parent.update_size(self.size)

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.size = 0

    def update_size(self,s):  
        self.size += s
        if self.parent:
            self.parent.update_size(s)

    def get_dir(self, name):
        for ch in self.children:
            if ch.name == name:
                return ch

    def add_dir(self, name, parent):
        self.children.append(Directory(name, parent))
    
    def add_file(self, name, size, parent):
        self.children.append(File(name, size, parent))

root = Directory('/', None)
cd = None

def do_cd(d):
    global cd 
    if d == "/":
        cd = root
    elif d == "..":
        cd = cd.parent
    else:
        cd = cd.get_dir(d)

def get_dir_with_size(dirs, dir, min, max):
    if dir.size <= max and dir.size >= min:
        dirs.append(dir)
    for ch in dir.children:
        if isinstance(ch, Directory):
            dirs = get_dir_with_size(dirs, ch, min, max)
    return dirs

#build the tree
lines = open("test.txt").read().splitlines()
for line in lines:
    if line.startswith("$ cd"):
        do_cd(line.split()[-1])
    elif line.startswith("$ ls"):
        continue
    elif line.startswith("dir"):
        cd.add_dir(line.split()[-1],cd)
    else:
        cd.add_file(line.split()[-1],int(line.split()[0]),cd)

#part one
total = 0
for node in get_dir_with_size([], root, 0, 100000):
    total +=  node.size   
print(total) 

#part two
current_used = 70000000 - root.size
need_free = 30000000 - current_used

delete = current_used
for node in get_dir_with_size([], root, need_free, current_used):
    if node.size < delete:
        delete =  node.size   
print(delete) 