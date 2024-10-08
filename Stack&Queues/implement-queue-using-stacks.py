class MyQueue:

    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        while len(self.stack1)!=0:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        while len(self.stack2)!=0:
            self.stack1.append(self.stack2.pop())
    def pop(self) -> int:
        if len(self.stack1)!=0:
            return self.stack1.pop()

    def peek(self) -> int:
        if len(self.stack1)!=0:
            return self.stack1[-1]
    def empty(self) -> bool:
        return len(self.stack1)==0
        
