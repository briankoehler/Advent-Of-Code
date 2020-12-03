
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = int(Lines[i].strip())
    
i = 0
first = 0
second = 0
third = 0
while (i < len(Lines)):
    first = Lines[i]
    j = i + 1
    while (j < len(Lines)):
        second = Lines[j]
        k = j + 1
        while (k < len(Lines)):
            third = Lines[k]
            if (first + second + third == 2020):
                print(f'{first * second * third}')
            k += 1
        j +=1
    i += 1
    