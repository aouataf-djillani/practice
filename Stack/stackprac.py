class Node:
    def __init(self, data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    
    """
    push new node before the head
    """
    def push(self, data):
        new=Node(data)
        if self.head==None:

            self.head=new  
        else: 
            #add data before head
            new.next=self.head 
            self.head=new

    """
    pop: remove the head
    """
    
    def pop(self,data):
        current=self.head
        self.head.next=None 
        self.head=current.next 

        


class queue(self):
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self,val):
        new=Node(val)
        if self.tail==None:
            self.head=self.tail=new
        else:
            self.tail.next=new
            self.tail=new

    def dequeue(self):
        if self.head is None:
            return 
        else: 
            current=self.head
            self.head.next=None
            self.head=current.next