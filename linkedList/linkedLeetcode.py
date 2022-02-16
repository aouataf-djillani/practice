class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0
    def get(self, index):
        

        if self.head is None:
            return -1
        
            
        if index<=self.size:
        
            found=False
            current = self.head
            count = 0
            while current != None and not found:
                if index == count:
                    return current.val
                    found=True
                count += 1
                current = current.next
        return -1

    def addAtHead(self, val):
        newNode = ListNode(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        newNode = ListNode(val)
        current = self.head
        if self.head==None:
            self.head=newNode
            self.size += 1
        
            
        else:
            
            while current.next:
                current=current.next
            current.next = newNode
            self.size += 1
        
    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            count = 0
            current = self.head
            prev = None
            newNode = ListNode(val)
            while count != index and current:
                
                prev = current
                current = current.next
                count += 1
            if count == index:
                prev.next = newNode 
                newNode.next = current
                self.size += 1

    def deleteAtIndex(self, index):
        if index == 0:
            ans = self.head.val
            newHead = self.head.next
            self.head = newHead
            self.size -= 1
            return ans
        else:
            count = 0
            current = self.head
            prev = None
            while count != index and current.next != None:
                prev = current
                current = current.next
                count += 1
            if count == index:    
                prev.next = current.next 
                self.size -= 1



        


obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
obj.addAtIndex(1,2)
print(obj.get(1))

obj.deleteAtIndex(1)
print(obj.get(1))




