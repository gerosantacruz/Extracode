x = 9
n = [10,20,20,10,10,30,50,10,20]


from collections import Counter

def sockMerchant(n,arr):
    n = Counter(arr)
    s = 0
    for i in n.values():
        s+=i//2
    return s

print(sockMerchant(x,n))