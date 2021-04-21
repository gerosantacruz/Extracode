def twoStrings(s1, s2):
    for letter in s1:
        if letter in s2:
            return "Yes"
            break
    else:
        return "NO"


print(twoStrings("ert","and"))