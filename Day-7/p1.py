
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    

class Bag:
    def __init__(self, name, bags):
        self.name = name
        self.bags = bags


all_bags = []
good_bags = set()


for line in Lines:
    
    split_line = line.split()
    bag_name = split_line[0] + ' ' + split_line[1]
    contains = []
    
    i = 0
    while i < len(split_line):
        if split_line[i].isdigit():
            contains_name = split_line[i + 1] + ' ' + split_line[i + 2]
            contains.append(contains_name)
        i += 1

    new_bag = Bag(bag_name, contains)
    all_bags.append(new_bag)

for bag in all_bags:
    if 'shiny gold' in bag.bags:
        good_bags.add(bag)

to_add = set()
for x in range(7):
    for b in good_bags:
        for bag in all_bags:
            if b.name in bag.bags:
                to_add.add(bag)
    for b in to_add:
        good_bags.add(b)
        
        
print(len(good_bags))
