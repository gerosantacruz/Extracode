def sumPairs(ints, s):
    cache = set()
    for i in ints:
        print(cache)
        if s - i in cache:
            return [s-i, i]
        cache.add(i)



ints = [10, 5, 2, 3, 7, 5]
s = 10

print(sumPairs(ints,s))

    