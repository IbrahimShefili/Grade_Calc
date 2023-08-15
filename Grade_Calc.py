#Grade Calculator
file = open('note.txt','r',encoding='utf-8')
for i in file:
    note1 = i.split(',')[1]
    note2 = i.split(',')[2]
    note3 = i.split(',')[3]
    last_note = round((int(note1)+int(note2)+int(note3))/3,2)
    note_alp = ''
    if last_note <= 50:
        note_alp = 'F'
    elif last_note <= 60 and last_note > 50:
        note_alp = 'E'
    elif last_note > 70 and last_note <= 80:
        note_alp = 'c'
    elif last_note > 80 and last_note <= 90:
        note_alp = 'B'
    elif last_note > 90:
        note_alp = 'A'
    print(i.split(',')[0],'======================>',note_alp)

    if note_alp == 'F':
        fail = open('failed.txt','a')
        fail.write(i.split(',')[0])
        fail.write('\n')
    else:
        pas = open('pass.txt','a')
        pas.write(i.split(',')[0])
        pas.write('\n')
        
        
        

















