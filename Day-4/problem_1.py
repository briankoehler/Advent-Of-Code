
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
    for k in current:
        if k != 'cid':
            if current[k] == False:
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
        current[l[:3]] = True
        
if is_complete():
    correct += 1

print(correct)
