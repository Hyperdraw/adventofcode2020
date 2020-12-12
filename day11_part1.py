with open('input11.txt', 'r') as file:
    puzzle = [list(line) for line in file.read().strip().splitlines()]

def run(ref):
    changed = False

    for x in range(len(ref)):
        for y in range(len(ref[x])):
            if ref[x][y] in ('#', 'L'):
                neighbors = 0

                for offset_x in range(-1, 2):
                    for offset_y in range(-1, 2):
                        if (offset_x or offset_y) and x + offset_x >= 0 and x + offset_x < len(ref) and y + offset_y >= 0 and y + offset_y < len(ref[x]) and ref[x + offset_x][y + offset_y] == '#':
                            neighbors += 1

                if ref[x][y] == 'L' and neighbors == 0:
                    puzzle[x][y] = '#'
                    changed = True
                elif ref[x][y] == '#' and neighbors >= 4:
                    puzzle[x][y] = 'L'
                    changed = True
    
    return changed

while run([row[:] for row in puzzle]):
    pass

occupied = 0

for row in puzzle:
    for seat in row:
        if seat == '#':
            occupied += 1

print(occupied)