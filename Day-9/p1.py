
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = int(Lines[i].strip())
    
    
for i in range(len(Lines)):

    if i < 25:
        continue
    
    current_number = Lines[i]
    validated = False
    
    subset = Lines[i - 25 : i]
    for first_num in subset:
        for second_num in subset:
            
            if second_num == first_num:
                continue
            
            if first_num + second_num == current_number:
                validated = True
                break
                
    if not validated:
        print(current_number)
        break