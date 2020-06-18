import sys

total = 0

for i in range(1000):
    if i % 15 == 0:
       total += i
    elif i % 5 == 0:
        total += i
    elif i % 3 == 0:
        total += i 

def test(result):
    if result == 233168:
        print("The result are correct!") 

test(total)
