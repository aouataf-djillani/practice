class Node:
     
    
    def __init__(self,data):
        self.data = data
        self.next = None     
class Stack:
     
    def __init__(self):
        self.head = None

    def __repr__(self):
        current=self.head
        L=[]
        while current:
            L.append(f"{current.data}")
            current=current.next

        return "=>".join(L)
    
    def push(self,val):
        #check if list is empty==>add element as head
        if self.head is None:
            self.head=Node(val)
        else:
            new=Node(val)
            new.next=self.head
            self.head=new
        return self.head

    def pop(self):
        if self.head is None:
            return -1
        else: 
            current=self.head
            self.head=self.head.next
            current.next=None
           
        return current.data


S1=Stack()
S1.push(5)
S1.push(6)
S1.push(6)
S1.push(6)
S1.push(6)
S1.pop()
S1.pop()

print(S1)

s1=[1,2,3,4]
s1.append(5)
print(s1)
s1.pop()
print(s1)