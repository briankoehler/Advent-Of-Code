
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
Lines.append('')

counts = []
current_questions = set()
is_first = True

for line in Lines:
    if line == '':
        counts.append(len(current_questions))
        current_questions = set()
        is_first = True
        continue
    
    if is_first:
        for ch in line:
            current_questions.add(ch)
        is_first = False
        continue
    
    remove = []
    for q in current_questions:
        if not q in line:
            remove.append(q)
            
    for q in remove:
        current_questions.remove(q)


print(sum(counts))
