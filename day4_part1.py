from re import split, findall

with open('input4.txt', 'r') as file:
    puzzle = split(r'\n\s*\n', file.read().strip())

count = 0

for passport in puzzle:
    fields = [pair.split(':')[0] for pair in split(r'\s+', passport)]
    valid = True

    for field in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'):
        if field not in fields:
            valid = False
            break
    
    if valid:
        count += 1

print(count)