def same_structure_as(original, other):
    if type(original) != type(other) or len(original) != len(other):
        return False
    for x, i in zip(original, other):
        if type(x) != type(i):
            return False
        if type(x) is list and type(i) is list:
            if not same_structure_as(x,i):
                return False
    return True




#true
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))

# should return False 
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] ))