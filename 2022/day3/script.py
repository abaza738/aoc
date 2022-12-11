
def get_priority(s: str) -> int:
    return ord(s)-96 if s.islower() else ord(s)-38

def get_similar_items(*args) -> set:
    found = []
    for i in args:
        found.append(set(i))
    result: set = found[0]
    for i in found:
        result = result.intersection(i)
    return result


with open('./input.txt', 'r') as read:
    lines = read.readlines()

summation_1 = 0
summation_2 = 0

# Part 1 loop
for line in lines:
    line = line.strip('\n')

    shared_item = list(get_similar_items(line[:int(len(line) / 2)], line[int(len(line) / 2):]))

    if not shared_item:
        continue

    summation_1 += get_priority(shared_item[0])

# Part 2 loop
for i in range(0, len(lines), 3):
    [line1, line2, line3] = [lines[i].strip('\n') for i in range(i, i+3)]

    shared_item_in_group = list(get_similar_items(line1, line2, line3))

    if not shared_item_in_group:
        raise Exception('Oepsie doepsie!')
    
    summation_2 += get_priority(shared_item_in_group[0])

print(summation_1)
print(summation_2)