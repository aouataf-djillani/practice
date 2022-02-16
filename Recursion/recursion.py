def sum(arr):
    if not arr:
        return 0
    
    return arr[0]+sum(arr[1:])
arr=[2, 5, 7, 4, 6]
print(sum(arr))

def ascending(arr):
    if len(arr)<1:
        return False
    
    return arr[0]< arr[1] and ascending(arr[1:])
arr1=[1,2,3,4]
print(ascending(arr1))