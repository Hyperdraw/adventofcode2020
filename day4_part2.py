from re import split, findall, match

with open('input4.txt', 'r') as file:
    puzzle = split(r'\n\s*\n', file.read().strip())

count = 0

for passport in puzzle:
    fields = {pair.split(':')[0]: pair.split(':')[1] for pair in split(r'\s+', passport)}
    valid = True

    valid = valid and 'byr' in fields and match(r'^\d{4}$', fields['byr']) != None and 1920 <= int(fields['byr']) <= 2002
    valid = valid and  'iyr' in fields and match(r'^\d{4}$', fields['iyr']) != None and 2010 <= int(fields['iyr']) <= 2020
    valid = valid and 'eyr' in fields and match(r'^\d{4}$', fields['eyr']) != None and 2020 <= int(fields['eyr']) <= 2030
    
    if 'hgt' in fields:
        hgtMatch = match(r'^(\d+)((?:cm)|(?:in))$', fields['hgt'])
        valid = valid and hgtMatch != None and hgtMatch[2] in ('cm', 'in') and ((hgtMatch[2] == 'cm' and 150 <= int(hgtMatch[1]) <= 193) or (hgtMatch[2] == 'in' and 59 <= int(hgtMatch[1]) <= 76))
    else:
        valid = False
    
    valid = valid and 'hcl' in fields and match(r'^#[0-9a-f]{6}$', fields['hcl']) != None
    valid = valid and 'ecl' in fields and fields['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    valid = valid and 'pid' in fields and match(r'^\d{9}$', fields['pid']) != None

    if valid:
        count += 1

print(count)