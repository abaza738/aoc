thing = []
elf_index = 0
maximum = 0

with open('./input.txt', 'r') as r:
    lines = r.read().split('\n')

for i in range(len(lines)):
    lines[i] = lines[i].strip('\n')
    if not lines[i]:
        elf_index += 1
        continue
    try:
        thing[elf_index] += int(lines[i])
    except IndexError:
        thing.append(int(lines[i]))
    finally:
        if thing[elf_index] > maximum:
            maximum = thing[elf_index]

# Part one solution
print(maximum)

thing.sort()

# Part two solution
print(sum(thing[-3:]))