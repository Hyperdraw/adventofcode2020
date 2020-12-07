from re import match

with open('input7.txt', 'r') as file:
    puzzle = file.read().strip().splitlines()

rules = {}

for line in puzzle:
    rule = match(r'^(\w+\s+\w+)\s+bags\s+contain\s+(.+)\.$', line)
    rules[rule[1]] = [match(r'\s*(\d+)\s*(\w+\s+\w+)\s+bags?', inner) for inner in rule[2].split(',')]

def count(color):
    n = 1

    for inner in rules[color]:
        if inner != None:
            n += count(inner[2]) * int(inner[1])
    
    return n

print(count('shiny gold') - 1)