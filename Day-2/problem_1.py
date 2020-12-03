import re

file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    
passwords = []
for line in Lines:
    passwords.append(re.split(r'[-\s]|:\s', line))
    
valid_count = len(passwords)

for password in passwords:
    char = password[2]
    count = 0
    for c in password[3]:
        if c == char:
            count += 1
            if count > int(password[1]):
                valid_count -= 1
                break
    if count < int(password[0]):
        valid_count -= 1
        
print(valid_count)