with open('2022/day8/input.txt', 'r') as r:
    lines = r.readlines()

data: list[list[int]] = []

for row_index in range(len(lines)):
    col = lines[row_index].strip('\n')
    data.append([])

    for col_index in range(len(col)):
        data[row_index].append(int(lines[row_index][col_index]))

visible_count = len(data)*4 - 4 # Initial data -> trees on the edges are already visible

def is_visible(data, row, col):
    tree = data[row][col]

    def is_visible_vertical(start, end):
        for index in range(start, end):
            if data[index][col] >= tree:
                return False
        return True

    def is_visible_horizontal(start, end):
        for index in range(start, end):
            if data[row][index] >= tree:
                return False
        return True
    
    return (
        is_visible_vertical(0, row) or
        is_visible_vertical(row+1, len(data)) or
        is_visible_horizontal(0, col) or
        is_visible_horizontal(col+1, len(data))
    )

# Only look at the inner trees, skip edges
for i in range(1, len(data)-1):
    for j in range(1, len(data)-1):
        if is_visible(data, i, j):
            visible_count += 1

print(visible_count)