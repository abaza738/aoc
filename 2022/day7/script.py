import re
from functools import reduce

MAX = 100000
TOTAL_SPACE = 70000000
UNUSED_TARGET = 30000000


class Node:
    def __init__(self, name: str, parent: str = None) -> None:
        self.name = name
        self.parent = parent

    def __str__(self) -> str:
        return self.name


class Directory(Node):
    def __init__(self, name: str, parent: str = None) -> None:
        super().__init__(name, parent)
        self.children: list[Node] = []

    def size(self):
        return reduce(lambda x, y: x + y.size(), self.children, 0)

    def append_child(self, node: 'Node'):
        self.children.append(node)


class File(Node):
    def __init__(self, name: str, size: int, parent: str = None) -> None:
        super().__init__(name, parent)
        self._size = size

    def size(self):
        return self._size


class Tree:
    root: Directory

    def __init__(self, root: Directory) -> None:
        self.root = root

    def __iter__(self,):
        stack = []
        stack.append(self.root)
        while len(stack) != 0:
            node = stack.pop()
            yield node
            if isinstance(node, Directory):
                stack += node.children

with open('./input.txt', 'r') as f:
    lines = f.readlines()

current_directory: Directory = None
tree: Tree = None

for line in lines:
    line = line.strip('\n')
    
    if re.match(r'\$ ls', line):
        continue

    if re.match(r'\$ cd ', line):
        directory_name = line.split(' ')[2]

        if directory_name == '..':
            current_directory = current_directory.parent
            continue
        elif directory_name == '/':
            root = Directory('/')
            tree = Tree(root)
            current_directory = root
            continue

        node = next((directory for directory in current_directory.children if directory.name == directory_name), None)

        if not node:
            raise NameError(f'Directory {directory_name} does not exist in {current_directory.name}')

        current_directory = node
        continue

    if re.match(r'dir ', line):
        new_directory = line.split(' ')[1]
        directory = Directory(new_directory, parent=current_directory)
        current_directory.append_child(directory)
        continue

    if re.match(r'(\d+) (\w+)', line):
        (size, name) = line.split(' ')
        file = File(name, int(size))
        current_directory.append_child(file)
        continue

total_size = 0
filled_space = tree.root.size()
free_space = TOTAL_SPACE - filled_space
smallest = filled_space # Initial value -> largest directory

for i in tree:
    if isinstance(i, File):
        continue
    size = i.size()

    # Part 1
    if size < MAX:
        total_size += size

    # Part 2
    if free_space + size > UNUSED_TARGET and size < smallest:
        smallest = size

print(total_size)
print(smallest)
