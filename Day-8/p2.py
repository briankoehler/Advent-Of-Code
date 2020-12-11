import copy

file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip().split()


i = 0
while i < len(Lines):
    
    new_code = copy.deepcopy(Lines)
    
    command = Lines[i][0]
    arg = Lines[i][1]
    
    if command == 'jmp':
        new_code[i][0] = 'nop'
    elif command == 'nop':
        new_code[i][0] = 'jmp'
        
    j = 0
    acc = 0
    executed = []
    while j < len(new_code):
        if j in executed:
            break
        executed.append(j)
        if new_code[j][0] == 'jmp':
            j += int(new_code[j][1])
            continue
        if new_code[j][0] == 'acc':
            acc += int(new_code[j][1])
        j += 1
    if j == len(new_code):
        print(acc)
    
    i += 1