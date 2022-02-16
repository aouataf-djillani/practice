from linked import linked
def mergeSort(linkedList):
    """
    - recursively divide into sublists until sublist with single node 
    -repeatedly merge while sorting 
    """
    if linkedList.length()<=1:
        return linkedList
    mid=linkedList.length()//2
    midNode=linkedList.searchByIndex(mid-1)
    left=linkedList
    right=linked()
    right.head=midNode.nextNode
    #cut the link between the two lists 
    midNode.nextNode=None
    """
    Merging
    """
    


    











l=linked()


print(mergeSort(l))


