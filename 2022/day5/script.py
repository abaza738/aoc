import re

stack = {
    '1': ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
    '2': ['H', 'F', 'R'],
    '3': ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
    '4': ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
    '5': ['P', 'S', 'M', 'J', 'H'],
    '6': ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
    '7': ['P', 'T', 'H', 'N', 'M', 'L'],
    '8': ['F', 'D', 'Q', 'R'],
    '9': ['D', 'S', 'C', 'N', 'L', 'P', 'H'],
}

with open('./input.txt', 'r') as f:
    lines = f.readlines()

regex = r'(\d+)'

# Part 1
# for line in lines:
#     instruction = re.findall(regex, line)
#     for i in range(int(instruction[0])):
#         stack[instruction[2]].append(stack[instruction[1]].pop())

# Part 2
for loine in lines:
    instruction = re.findall(regex, loine)
    temp = []
    for i in range(int(instruction[0])):
        temp.append(stack[instruction[1]].pop())
    temp.reverse()
    stack[instruction[2]] += temp


for key in stack.keys():
    print(stack[key][len(stack[key])-1])