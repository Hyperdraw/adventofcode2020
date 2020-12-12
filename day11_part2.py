with open('input11.txt', 'r') as file:
    puzzle = [list(line) for line in file.read().strip().splitlines()]

def ray(ref, start_x, start_y, offset_x, offset_y):
    i = 1

    while True:
        x = start_x + offset_x * i
        y = start_y + offset_y * i

        if x < 0 or x >= len(ref) or y < 0 or y >= len(ref[x]) or ref[x][y] == 'L':
            return False
        elif ref[x][y] == '#':
            return True
        
        i += 1

def run(ref):
    changed = False

    for x in range(len(ref)):
        for y in range(len(ref[x])):
            if ref[x][y] in ('#', 'L'):
                neighbors = 0

                for offset_x in range(-1, 2):
                    for offset_y in range(-1, 2):
                        if (offset_x or offset_y) and ray(ref, x, y, offset_x, offset_y):
                                neighbors += 1

                if ref[x][y] == 'L' and neighbors == 0:
                    puzzle[x][y] = '#'
                    changed = True
                elif ref[x][y] == '#' and neighbors >= 5:
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