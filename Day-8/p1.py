
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    

acc = 0
i = 0
executed = []
while i < len(Lines):
    
    if i in executed:
        break
    executed.append(i)
    
    command = Lines[i].split()[0]
    arg = Lines[i].split()[1]
    
    if command == 'jmp':
        i += int(arg)
        continue
    if command == 'acc':
        acc += int(arg)
    i += 1
    
print(acc)