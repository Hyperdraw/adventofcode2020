with open('input1.txt', 'r') as file:
    puzzle = [int(line) for line in file.read().strip().splitlines()]

for i in puzzle:
    for j in puzzle:
        if i != j:
            for k in puzzle:
                if k not in (i, j) and i + j + k == 2020:
                    print(i * j * k)
                    exit()