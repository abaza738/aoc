# Part 1 and part 2 differ in window size!
# Use 4 for part 1, and 14 for part 2
WINDOW_SIZE = 14

with open('2022/day6/input.txt', 'r') as f:
    message = f.readline().strip('\n')

queue = [*message[:WINDOW_SIZE - 1]]

for i in range(WINDOW_SIZE - 1, len(message)):
    queue.append(message[i])
    has_duplicates = False
    temp = []
    for char in queue:
        if char in temp:
            has_duplicates = True
            break
        temp.append(char)
    if not has_duplicates:
        print(i+1)
        break
    queue.pop(0)
