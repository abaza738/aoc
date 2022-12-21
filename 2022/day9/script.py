
grid = {}

with open('./input.txt', 'r') as r:
    lines = r.readlines()

nodes = {
    'head': {
        'x': 0,
        'y': 0
    },
    'tail': {
        'x': 0,
        'y': 0,
    }
}

def move_node(direction: str, magnitude: int, node: str=None):
    axis = None
    sign = 1
    match direction:
        case 'U':
            axis = 'y'
        case 'D':
            axis = 'y'
            sign = -1
        case 'R':
            axis = 'x'
        case 'L':
            axis = 'x'
            sign = -1

    for _ in range(magnitude):
        nodes[node][axis] += sign*1

        if node == 'tail':
            return

        is_adjacent = is_touching(nodes['head'], nodes['tail'])
        if is_adjacent:
            continue
        move_tail()

def move_tail():
    vertical_distance = nodes['head']['y'] - nodes['tail']['y']
    horizontal_distance = nodes['head']['x'] - nodes['tail']['x']

    if horizontal_distance == 0:
        move_node('U' if vertical_distance > 0 else 'D', 1, 'tail')
    elif vertical_distance == 0:
        move_node('R' if horizontal_distance > 0 else 'L', 1, 'tail')
    elif (abs(horizontal_distance) > 1) or (abs(vertical_distance) > 1):
        move_node('U' if vertical_distance > 0 else 'D', 1, 'tail')
        move_node('R' if horizontal_distance > 0 else 'L', 1, 'tail')

    grid[f"{nodes['tail']['x']},{nodes['tail']['y']}"] = 1

def is_touching(first, second):
    return (abs(first['x'] - second['x']) <= 1) and (abs(first['y'] - second['y']) <= 1)

for line in lines:
    line = line.strip('\n')

    (direction, mag) = line.split(' ')

    move_node(direction, int(mag), 'head')

print(len(grid.keys()) + 1)
