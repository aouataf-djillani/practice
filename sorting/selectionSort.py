def selectionSort(arr):
    for i in range(len(arr)):
        min=i
        print(min)
        for j in range(1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        
        arr[i],arr[min]=arr[min],arr[i]
        return arr

arr=[5,2,7,4,6]
print(selectionSort(arr))