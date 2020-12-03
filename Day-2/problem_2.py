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
    first_index = False
    second_index = False
    if password[3][int(password[0]) - 1] == password[2]:
        first_index = True
    if password[3][int(password[1]) - 1] == password[2]:
        second_index = True
    if first_index and second_index:
        valid_count -= 1
    if not first_index and not second_index:
        valid_count -= 1

print(valid_count)