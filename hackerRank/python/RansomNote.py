
def ransom_note(magazine, rasom):
    hash_note = {}

    for i in magazine:
        if hash_note.get(i) != None:
            if (hash_note[i] > 0):
                hash_note[i] += 1
        else:
            hash_note[i] = 1

    for x in rasom:
        if hash_note.get(x) == None or hash_note.get(x) == 0:
            return 'No'
        else:
            hash_note[x] -= 1
    return 'Yes'

print(ransom_note('attack at dawn', 'Attack at dawn'))

