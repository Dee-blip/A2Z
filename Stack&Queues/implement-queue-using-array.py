class MyQueue:
    
    def __init__(self):
        self.queue=[]
    #Function to push an element x in a queue.
    def push(self, x):
        return self.queue.append(x)
         
    #Function to pop an element from queue and return that element.
    def pop(self):
        if not self.queue:
            return -1
        return self.queue.pop(0)
