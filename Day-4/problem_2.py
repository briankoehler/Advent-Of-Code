import re

file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    
    
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

current = {
    'byr': False,
    'iyr': False,
    'eyr': False,
    'hgt': False,
    'hcl': False,
    'ecl': False,
    'pid': False,
    'cid': False
}

def reset():
    for k in current:
        current[k] = False
        
def is_complete():
    print(current)
    for k in current:
        if k != 'cid':
            if current[k] == False:
                return False
    return True

def is_valid(field, value):
    if field == 'byr':
        if len(value) != 4 or not value.isdigit() or int(value) < 1920 or int(value) > 2002:
            return False
    if field == 'iyr':
        if len(value) != 4 or not value.isdigit() or int(value) < 2010 or int(value) > 2020:
            return False
    if field == 'eyr':
        if len(value) != 4 or not value.isdigit() or int(value) < 2020 or int(value) > 2030:
            return False
    if field == 'hgt':
        if value[-2:] != 'in' and value[-2:] != 'cm':
            return False
        if not value[:-2].isdigit():
            return False
        if value[-2:] == 'cm':
            if int(value[:-2]) < 150 or int(value[:-2]) > 193:
                return False
        if value[-2:] == 'in':
            if int(value[:-2]) < 59 or int(value[:-2]) > 76:
                return False
    if field == 'hcl':
        if not value[:1] == '#':
            return False
        pattern = re.compile('[a-f0-9]+')
        zach_is_ned = value[1:]
        if len(zach_is_ned) != 6:
            return False
        if not pattern.match(zach_is_ned):
            return False
    if field == 'ecl':
        options = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not value in options:
            return False
    if field == 'pid':
        if len(value) != 9 or not value.isdigit():
            return False
    return True

correct = 0

for line in Lines:
    if line == '':
        if is_complete():
            correct += 1
        reset()
        continue
    line_list = line.split()
    for l in line_list:
        current[l[:3]] = is_valid(l[:3], l[4:])
        
if is_complete():
    correct += 1

print(correct)
