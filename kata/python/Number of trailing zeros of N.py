#force brute way
import math

fact= math.factorial(11)

trail = str(fact)

temp1= 0

temp2 = 0

for i in trail:
    if(i == '0'):
        temp1 +=1
        
    elif i != '0':
        temp2 = temp1
        temp1 = 0
    
print(temp1)

#mathematical way...
def findTrailingZeros(n): 
    
    # Initialize result 
    count = 0
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
    return int(count) 

print(findTrailingZeros(11))