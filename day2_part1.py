from re import match
from collections import Counter

with open('input2.txt', 'r') as file:
    puzzle = [match(r'(\d+)-(\d+)\s+(\w):\s*(.*)', line) for line in file.read().strip().splitlines()]

valid = 0

for password in puzzle:
    if int(password[1]) <= Counter(password[4])[password[3]] <= int(password[2]):
        valid += 1

print(valid)