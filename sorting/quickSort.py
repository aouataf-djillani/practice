def quickSort(arr):
    #base case: list empty or has one item 
    if len(arr)<=1:
        return arr

    #recursion case
    
    pivot=arr[0]
    left=[]
    right=[]
    for i in arr[1:]:
        if i<=pivot:
            left.append(i)
        else:
            right.append(i)
        
    return quickSort(left)+[pivot]+quickSort(right)

arr=[11, 3, 7, 5, 2, 77,1,90,12,67,8,4]
print(quickSort(arr))


