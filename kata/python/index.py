phrase = "abaaaaa"

letters = {}

unique = ''.join(set(phrase))

for _ in sorted(unique):
    if unique:
        letterTimes = phrase.count(_)
        letters.update({ _ : letterTimes})
    else:
        letters = {}

print(letters)
