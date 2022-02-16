class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
    
    def __repr__(self):
        return f"{self.data}"


class linked:
    
    def __init__(self):
        self.head=None
    """
    appending an item at the end of a linked list (edge case: empty list ie head is none 
    creat new node 
    traverse the list while current.next (it stops at element before last)
    turn current to current.next(last element) point from last to new node
    """
    def append(self, value):
        newNode=Node(value)
        if self.head is None:
            self.head=value
        current=self.head
        while current.nextNode:
            current=current.nextNode
        current.nextNode=newNode
    """
    set current to head while current pritn current data 
    keep moving to next node 
    """
    def iterate(self):
        current=self.head 
        while current:
            print(current.data)
            current=current.nextNode
    """
    set counter, traverse and increment counter by 1  
    """
    def size(self):
        current=self.head
        count=0
        while current:
            current=current.nextNode
            count+=1
        return count      
    """
    search by value: Traverse if current == value  return True keep traversing if not found
    """
    def search(self,item):
        current=self.head
        while current:
            if current.data==item:
                return True
            current=current.nextNode
        return False 
    """
    takes index returns value
    set position as index decrement while traversing until O when position is 0 return value (current.data)
    """
    def access(self,index):
        current=self.head
        
        position=index
        while position>=1:
            current=current.nextNode
            position-=1
       
        return f"found {current.data} at index: {index}"

    """
    deleting the first item of a list setting head to current.nextNode 
    """
    def deleteFirst(self):
        current=self.head
        self.head=current.nextNode
        return f"new head: {self.head}"
    
    """
    Traverse until last alement nextNode=Node
    go to previous and set next node to node 
    """
    def deleteLast(self):
        current=self.head 
    
        while (current.nextNode.nextNode):
            current=current.nextNode
        
        current.nextNode=None
        
        


        
    """
    preappend
    """
    def preappend(self,value):
        newNode=Node()
        newNode.nextNode=self.head
        self.head=newNode

    def append(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=value
        current=self.head
        while current.nextNode:
            current=current.nextNode
        current.nextNode=newNode
    
  


    """
    traversing while adding current.data to a list resturn the joined list as a string 
    """
    def __repr__(self) -> str:
        arr=[]
        current=self.head

        while current:
            arr.append(f"{current.data}")
            current=current.nextNode
        return "->".join(arr)
    def delete (self,key):
        current=self.head
        previous=None
        found=False
        while current and not found:
            if current.data ==key and current is self.head:
                found=True
                self.head=current.nextNode
            elif current.data==key:
                found=True
                previous.nextNode = current.nextNode
            else:
                previous=current
                current=current.nextNode
        return current
l=linked()
l.append(Node(1))
l.append(Node(10))
l.append(Node(12))
l.append(Node(10))

print(l)
l.delete(10)
print(l)