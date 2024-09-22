from queue import Queue
class MyStack:

    def __init__(self):
        self.q1= Queue()
        self.q2= Queue()
            
    def push(self, x: int) -> None:
        self.q2.put(x)
        print('Outer',self.q2)
        while(not self.q1.empty()):
            self.q2.put(self.q1.queue[0])
            self.q1.get()
            # print('Inside q1',q1)
            
        self.q1,self.q2= self.q2,self.q1

    def pop(self) -> int:
        if (self.q1.empty()):
            return 
        return self.q1.get()
        
        

    def top(self) -> int:
        if (self.q1.empty()):
            return -1
        return self.q1.queue[0]
        

    def empty(self) -> bool:
        return self.q1.qsize()==0      


class MyStack:

    def __init__(self):
        self.q1=[]

    def push(self, x: int) -> None:
        self.q1.append(x)

        for i in range(len(self.q1)-1):
            self.q1.append(self.q1[0])
            self.q1.pop(0)
        print(self.q1)
        return self.q1
        
    def pop(self) -> int:
        if len(self.q1)!=0:
            return self.q1.pop(0)
        return None

    def top(self) -> int:
        if len(self.q1)!=0:
            return self.q1[0]
        return None
        

    def empty(self) -> bool:
        return len(self.q1)==0
        
