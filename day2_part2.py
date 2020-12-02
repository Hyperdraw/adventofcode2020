from re import match

with open('input2.txt', 'r') as file:
    puzzle = [match(r'(\d+)-(\d+)\s+(\w):\s*(.*)', line) for line in file.read().strip().splitlines()]

valid = 0

for password in puzzle:
    count = 0

    if password[4][int(password[1]) - 1] == password[3]:
        count += 1
    
    if password[4][int(password[2]) - 1] == password[3]:
        count += 1

    if count == 1:
        valid += 1

print(valid)