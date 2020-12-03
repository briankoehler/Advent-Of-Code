
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()

pairs = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

product = 1

for pair in pairs:
    x = 0
    y = 0
    count = 0
    x_change = pair[0]
    y_change = pair[1]
    while (y < len(Lines)):
        if Lines[y][x] == '#':
            count += 1
        y += y_change
        x += x_change
        if x >= len(Lines[0]):
            x = x - len(Lines[0])
    product *= count
        
print(product)