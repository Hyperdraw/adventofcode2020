with open('input9.txt', 'r') as file:
    puzzle = [int(line) for line in file.read().strip().splitlines()]

def valid(n, addends):
    for a in addends:
        for b in addends:
            if a != b and a + b == n:
                return True
    
    return False

for i in range(25, len(puzzle)):
    if not valid(puzzle[i], puzzle[i - 25:i]):
        print(puzzle[i])
        break