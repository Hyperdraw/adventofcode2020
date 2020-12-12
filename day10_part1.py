with open('input10.txt', 'r') as file:
    puzzle = [int(line) for line in file.read().strip().splitlines()]

used = 0
adapter = 0
counts = {1: 0, 2: 0, 3: 1}

while used < len(puzzle):
    for diff in (1, 2, 3):
        found = False

        for option in puzzle:
            if option - adapter == diff:
                adapter = option
                used += 1
                found = True
                break
        
        if found:
            counts[diff] += 1
            break

print(counts)