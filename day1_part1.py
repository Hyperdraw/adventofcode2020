with open('input1.txt', 'r') as file:
    puzzle = [int(line) for line in file.read().strip().splitlines()]

for i in puzzle:
    for j in puzzle:
        if i != j and i + j == 2020:
            print(i * j)
            exit()