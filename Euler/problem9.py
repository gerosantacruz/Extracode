"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def Triplets(target):
    for a in range(2,target):
        for b in range(a,target - a):
            c = target - a - b 

            if a ** 2 + b ** 2 == c ** 2:
                print('The result is {} + {} + {} = {}'.format(a,b,c,target))
                

Triplets(1000)
