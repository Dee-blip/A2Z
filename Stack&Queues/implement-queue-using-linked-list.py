# A linked list (LL) node 
# to store a queue entry 
class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    def __init__(self):
        self.start = None
        self.end=None
        self.count=1
    
    #Function to push an element into the queue.
    def push(self, item): 
        newNode = Node(item)
        if self.start==None:
            self.start= self.end=newNode 
        else:
            self.end.next = newNode
            self.end= newNode
        
            
        self.count+=1
        
    
    #Function to pop front element from the queue.
    def pop(self):
        if self.count==0 or self.start==None:
            return -1
        popped = self.start.data
        self.start = self.start.next
        self.count-=1
        return popped
        
