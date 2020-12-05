from math import floor, ceil

with open('input5.txt', 'r') as file:
    puzzle = file.read().strip().splitlines()

plane = {}

def seat_id(seat):
    rows = (0, 127)

    while seat[0] in ('F', 'B'):
        if seat[0] == 'F':
            rows = (rows[0], floor((rows[0] + rows[1]) / 2))
        elif seat[0] == 'B':
            rows = (ceil((rows[0] + rows[1]) / 2), rows[1])
        
        seat = seat[1:]
    
    columns = (0, 8)

    while seat != '':
        if seat[0] == 'L':
            columns = (columns[0], floor((columns[0] + columns[1]) / 2))
        elif seat[0] == 'R':
            columns = (ceil((columns[0] + columns[1]) / 2), columns[1])
        
        seat = seat[1:]
    
    return rows[0] * 8 + columns[0]

for seat in puzzle:
    plane[seat_id(seat)] = True

for x in range(8):
    for y in range(1, 127):
        sid = y * 8 + x

        if sid not in plane and (sid + 1) in plane and (sid - 1) in plane:
            print(sid)