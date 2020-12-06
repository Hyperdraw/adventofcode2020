from re import split, sub
from collections import Counter

with open('input6.txt', 'r') as file:
    puzzle = split(r'\s*\n\s*\n\s*', file.read().strip())

total = 0

for group in puzzle:
    total += len(Counter(sub(r'\s+', '', group)))

print(total)