def diagonalDifference(arr):
    sumleft = sum(arr[i][i] for i in range(len(arr)))    
    sumright = sum(arr[i][len(arr)-i-1] for i in range(len(arr)))
            
    difference = abs(sumleft-sumright)

    return difference


print(diagonalDifference([[1,2,3],[1,2,3],[1,2,3]]))