Names = [ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ]

print(len(Names))
nameL = []
title = ""
for i in Names:
    print(list(i.values()))
    nameL += list(i.values())

for i in nameL:
    if i == nameL[-1]:
        title += " & " + i
    elif i == nameL[-2]:
        title += i
    else:    
        title += i + " , "

print(title)        
