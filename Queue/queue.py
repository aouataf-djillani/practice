"""
Queue implementaion using linked list
"""

"""
node class with data and next attributes 
"""


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def __repr__(self):
        return f"{self.data}"

"""
the queue class with head and tail 
"""
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __repr__(self) -> str:
        arr=[]
        current=self.head

        while current:
            arr.append(f"{current.data}")
            current=current.next
        return "->".join(arr)



    def enqueue(self, val):
        """
        enqueuing is adding a node ater the tail and setting tai to new node 
        """
        new=Node(val)
        if self.tail is None:
            self.head=self.tail=new
            return
        else:

            self.tail.next=new
            self.tail=new
                      
        
    
    def dedequeue(self):
        """
        remove the head: set head to next node
        """
        if self.head is None:
            return 
        
        else:
            current=self.head
            self.head=self.head.next
            current.next=None 
        

Q1=Queue()
Q1.enqueue(5)
Q1.enqueue(6)
Q1.enqueue(6)
Q1.enqueue(6)
Q1.dedequeue()
print(Q1)
