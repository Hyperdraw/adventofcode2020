with open('input3.txt', 'r') as file:
    puzzle = file.read().strip().splitlines()

answer = 1

for slope in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
    x = 0
    y = 0
    trees = 0

    while y < len(puzzle) - slope[1]:
        x += slope[0]
        y += slope[1]

        if puzzle[y][x % len(puzzle[y])] == '#':
            trees += 1
    
    answer *= trees

print(answer)