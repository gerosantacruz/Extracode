a = [1,1,2,2,3]
birds = {1:0,2:0,3:0,4:0,5:0}



def migratoryBirds(arr):
    res = 0
    bird = 0 
    
    for i in arr:
        birds[i] += 1 
    
    for i in birds:
        if birds[i] > res:
            res = birds[i]
            bird = i

        
        
    return bird

kar = migratoryBirds(a)

print(kar)

#print(birds)