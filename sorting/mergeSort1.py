"""
    sorts a list in ascending order

    Step1: divide : find the mid point and divide into sublists
    step2: conquer recursively sort the sublist created in previous steps 
    step3 merge the sorted sublists created in previous step 

"""
def mergeSort(arr):
    """
    divide
    """
    if len(arr)<=1:
        return arr

    

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    mergeSort(left)
    mergeSort(right)
    """
    merges two sublists and sorts them in the process
    returns a new merge list 
    """
    #keep track of indexes
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1

        k+=1
    #when right list is shorter than left
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    #when left list is shorter that right 
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return arr    

arr=[11, 3, 7, 5, 2, 77,1,90,12,67,8,4]
arr1=[5,1,1,2,0,0]
print(mergeSort(arr1))

s
