import random

def isSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True 

def bogoSort(arr):
    while not isSorted(arr):
        random.shuffle(arr)
    return arr


