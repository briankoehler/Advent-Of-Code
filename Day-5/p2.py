
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    
    
def partition(string, poss):
    for ch in string:
        size = poss[1] - poss[0] + 1
        if ch == 'F' or ch == 'L':
            poss[1] -= size / 2
        elif ch == 'B' or ch == 'R':
            poss[0] += size / 2
    return poss[0]
        
ids = []

for line in Lines:
    row = partition(line[:7], [0, 127])
    column = partition(line[7:], [0, 7])
    
    seat_id = (row * 8) + column
    ids.append(seat_id)

ids.sort()

i = 0
while i != len(ids) - 1:
    if ids[i] + 2 == ids[i + 1]:
        print(ids[i] + 1)
    i += 1
