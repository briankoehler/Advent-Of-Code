
file = open('input.txt', 'r')
Lines = file.readlines()

for i in range(len(Lines)):
    Lines[i] = Lines[i].strip()
    
Lines.append('')
counts = []

current_questions = set()
for line in Lines:
    if line == '':
        counts.append(len(current_questions))
        current_questions.clear()
        continue
    for ch in line:
        current_questions.add(ch)

            
print(sum(counts))