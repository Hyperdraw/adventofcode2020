from re import split, sub
from collections import Counter

with open('input6.txt', 'r') as file:
    puzzle = split(r'\s*\n\s*\n\s*', file.read().strip())

total = 0

for group in puzzle:
    lines = len(group.splitlines())
    total += len([count for count in Counter(sub(r'\s+', '', group)).values() if count == lines])

print(total)