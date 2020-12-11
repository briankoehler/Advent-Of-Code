
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
            
all_dict = {}

for line in Lines:
    split_line = line.split()
    key = split_line[0] + ' ' + split_line[1]
    bag_dict = {}
    i = 0
    while i < len(split_line):
        if split_line[i].isdigit():
            bag_dict[split_line[i + 1] + ' ' + split_line[i + 2]] = [split_line[i]]
        i += 1
    all_dict[key] = bag_dict
    
base = all_dict['shiny gold']
for key in base:
    base[key].append(all_dict[key])
    
print(base)