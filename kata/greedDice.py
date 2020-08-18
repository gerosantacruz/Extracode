from collections import Counter
def greedDice(dices):
    a = Counter(dices)

    for i in a:
        print(i.value)

trow = [5,3,1,4,1]
#greedDice(trow)
print(Counter(trow.sort))
