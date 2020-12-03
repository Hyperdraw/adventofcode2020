with open('input3.txt', 'r') as file:
    puzzle = file.read().strip().splitlines()

x = 0
y = 0
trees = 0

while y < len(puzzle) - 1:
    x += 3
    y += 1

    if puzzle[y][x % len(puzzle[y])] == '#':
        trees += 1

print(trees)