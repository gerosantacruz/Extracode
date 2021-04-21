def repeatedString(s, n):
    k = s.count("a")*(n/len(s))
    k += s[:n%len(s)].count("a")

    return round(k)-1

print(repeatedString('aba',10))