from re import match

with open('input7.txt', 'r') as file:
    puzzle = file.read().strip().splitlines()

rules = {}

for line in puzzle:
    rule = match(r'^(\w+\s+\w+)\s+bags\s+contain\s+(.+)\.$', line)
    rules[rule[1]] = [match(r'\s*(\d+)\s*(\w+\s+\w+)\s+bags?', inner) for inner in rule[2].split(',')]

def can_contain(container, inner):
    for valid in rules[container]:
        if valid != None and (valid[2] == inner or can_contain(valid[2], inner)):
            return True
    
    return False

count = 0

for color in rules:
    if can_contain(color, 'shiny gold'):
        count += 1

print(count)