INVALID_NUM = 127 # REPLACE with the result of part one

with open('input9.txt', 'r') as file:
    puzzle = [int(line) for line in file.read().strip().splitlines()]

def valid(n, addends):
    for a in addends:
        for b in addends:
            if a != b and a + b == n:
                return True
    
    return False

def try_at(pos):
    for end in range(pos + 2, len(puzzle)):
        count = 0
        smallest = -1
        largest = 0

        for i in range(pos, end):
            count += puzzle[i]

            if smallest == -1 or puzzle[i] < smallest:
                smallest = puzzle[i]
            
            if puzzle[i] > largest:
                largest = puzzle[i]
        
        if count == INVALID_NUM:
            return smallest + largest
    
    return None

for i in range(len(puzzle) - 2):
    result = try_at(i)

    if result != None:
        print(result)