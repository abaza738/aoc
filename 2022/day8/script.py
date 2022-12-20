
with open('2022/day8/input.txt', 'r') as r:
    lines = r.readlines()

data: list[list[int]] = []

for row_index in range(len(lines)):
    col = lines[row_index].strip('\n')
    data.append([])

    for col_index in range(len(col)):
        data[row_index].append(int(lines[row_index][col_index]))

visible_count = 0

def is_visible_and_count(data: list[list[int]], row: int, col: int) -> tuple[bool, int]:
    tree = data[row][col]

    def is_visible_vertical(start, end, step=1):
        count = 0
        for index in range(start, end, step):
            count += 1
            if data[index][col] >= tree:
                return (False, count)
        return (True, count)

    def is_visible_horizontal(start, end, step=1):
        count = 0
        for index in range(start, end, step):
            count += 1
            if data[row][index] >= tree:
                return (False, count)
        return (True, count)

    top = is_visible_vertical(row-1, -1, -1)
    bottom = is_visible_vertical(row+1, len(data))
    left = is_visible_horizontal(col-1, -1, -1)
    right = is_visible_horizontal(col+1, len(data))

    
    return (
        top[0] or bottom[0] or left[0] or right[0],
        top[1] * bottom[1] * left[1] * right[1]
    )


def main():
    global visible_count
    max_score = 0

    for i in range(0, len(data)):
        for j in range(0, len(data)):
            result = is_visible_and_count(data, i, j)

            if result[1] > max_score:
                max_score = result[1]

            if result[0]:
                visible_count += 1
    print(visible_count, max_score)


if __name__ == "__main__":
    main()