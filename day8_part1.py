with open('input8.txt', 'r') as file:
    puzzle = [line.split(' ') for line in file.read().strip().splitlines()]

acc = 0
i = 0
ran = set()

while i not in ran:
    ran.add(i)

    if puzzle[i][0] == 'acc':
        acc += int(puzzle[i][1])
        i += 1
    elif puzzle[i][0] == 'jmp':
        i += int(puzzle[i][1])
    elif puzzle[i][0] == 'nop':
        i += 1

print(acc)