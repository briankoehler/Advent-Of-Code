
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    
x = 0
y = 0
count = 0

while (y < len(Lines)):
    if Lines[y][x] == '#':
        count += 1
    y += 1
    x += 3
    if x >= len(Lines[0]):
        x = x - len(Lines[0])
        
print(count)