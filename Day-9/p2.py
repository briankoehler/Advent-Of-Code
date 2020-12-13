
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = int(Lines[i].strip())
    
    
invalid_number = 0
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
        invalid_number = current_number
        break 


for i in range(len(Lines)):
    for j in range(len(Lines)):
        
        subset = Lines[i : i + j]
        if sum(subset) == invalid_number:
            print(min(subset) + max(subset))
            exit()