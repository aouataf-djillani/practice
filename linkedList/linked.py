class Node:
    """
    Create a node with data and reference to next node 
    """
    def  __init__(self, data):
        self.data=data
        self.nextNode=None

    """
    string representation of our node 
    """
    def __repr__(self) -> str:
        return f"<node: {self.data}>"


n1=Node(5)
print(n1) 
"""
    a linked list class 
    with a head 
"""
class linked:
    def __init__(self) -> None:
        self.head=None


    def isempty(self):
        return self.head==None

    """
    check length
    set current to head
    set counter 
    while current is not none: set current to next node increment counter by one a
    return counter  
        
    """

    def length(self):
        current=self.head
        counter=0
        while current != None:
            current=current.nextNode
            counter+=1
        return counter 
    
    """
    preappend: 
    set new node 
    set current to head 
    move head to new.next node
    set new node as head 
    """
    def add(self, data):
        new=Node(data)
        new.nextNode=self.head
        self.head=new
    """
    if index == 0 we preappend
    if index >0 define position as index define current as head define a new node 
    while position > 1 we move current to next node we decrement until we et to 1
    set prev as current 
    after as current.nextnode 
    set previous point to new and new point to after 
    """    
    def insert(self, data, index):
        if index==0:
            self.add(data)
        if index>0:

            current=self.head
            new= Node(data)
            position=index
        
            while position>1:
                current=current.nextNode
                position-=1

            prev=current
            nexto=current.nextNode

            prev.nextNode=new
            new.nextNode=nexto

    """
    delete a key value
    """
    def delete(self, key):
        
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
    def searchByIndex(self, index):
        if index==0:
            return self.head
        else:
            current=self.head
            position=0
            while position<index:
                current=current.nextNode
                position+=1
            return current
    """
    string representation
    create empty list 
    set current to head 
    traverse while current is not none  append each current as a string move current to nextnode
    """
    

    def __repr__(self) -> str:
        arr=[]
        current=self.head

        while current:
            arr.append(f"{current.data}")
            current=current.nextNode
        return "->".join(arr)

l=linked()
l.add(5)
l.add(6)
l.add(8)
l.add(9)
l.add(10)
l.insert(20,1)
l.insert(200,4)
l.insert(2000,2)
l.insert(200000,0)
l.delete(2000)
print(l)
print(l.isempty())
print(l.length())




