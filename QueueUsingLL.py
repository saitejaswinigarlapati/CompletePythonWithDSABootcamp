class Node():
    def __init__(self,value):
        self.data=value
        self.next=Node
        
class QueueUsingLL():
    def __init__(self):
        self.head=None
        self.tail=None
        self.len=0
    def size(self):
        return self.len
    
    def isEmpty(self):
        return self.size==0
    
    def enqueue(self,data):
        newNode=Node(data)
        self.len+=1
        if(self.head is None):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        return f"Added {data} to the Queue"
    
    def front(self):
        if(self.isEmpty()):
            print("Queue is empty, cannot show Front")
            return
        return self.head.data
    
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty, cannot Dequeue")
            return
        self.len-=1
        dataTobeReturned=self.head.data
        self.head=self.head.next
        if(self.head==None):
            self.tail==None
        return dataTobeReturned

Q=QueueUsingLL()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)

print(Q.size())  # 3
print(Q.isEmpty()) # False
print(Q.front())   # 10
print(Q.dequeue()) # 10
print(Q.dequeue()) # 20
print(Q.front())   #30
print(Q.size())  # 1