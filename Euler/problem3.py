"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def largestPrime(num, div=2):
    while div < num:
        print(num)
        if num % div == 0 and num/div > 1:
            num = num / div
            div = 2
        else:
            div = div + 1
    return num

#print(largestPrime(600851475143))
print(largestPrime(13))



