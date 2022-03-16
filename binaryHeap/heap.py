class MinHeap:
    """
    initialize the heap class with max capacity
    eg a heap with a capacity of 4 is: heap=[0,0,0,0]
    """
    def _init__(self, capacity):
        self.capacity=capacity 
        self.storage=[0]*capacity
        self.size=0 
    """  
    define helper methods:  
            *get parent node 
            *get left child node 
            *get right child node
    """
    def getParentIndex(self, index):
        return (index-1)//2 
    def getLeftChild(self, index):
        return 2*index+1
    def getRightChild(self,index):
        return 2*index+2

    """
    check if a node has a parent node: return true or false
    """
    def hasParent(self,index):
        #return (index-1)//2 >=0
        return self.getParentIndex(index)>=0

    """
    check if node has left child 
    """
    def hasLeftChild(self,index):
        return self.getLeftChild<self.size

    """
    check if node has right child 
    """
    def hasRightChild(self,index):
        return self.getRightChild<self.size
    
    """
    check if our heap is full before insertion 
    """
    def isFull(self):
        self.size==self.capacity

    """"
    swapping elements 
    """
    def swap(self, index1, index2): 
        temp=self.storage[index1]
        self.storage[index1]=self.storage[index2]
        self.storage[index2]=temp

    ########################
    #  inserting data      #
    ########################  
    def insert(self, data):
        if self.isFull():
            raise ("heap is full")
        #insert the data at the last element 
        self.storage[self.size]=data
        #we increment the size 
        self.size+=1
        self.heapifyUp() 

    def heapifyUp(self):
        index=self.size-1 #because we added the data to the index before and increased the size 
        #while our node has a parent and the parent is smaller we swap 
        while self.hasParent(index) and self.storage[self.getParentIndex(index)]>self.storage[index]:
            self.swap(self.getParentIndex(index), index)
