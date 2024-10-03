class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]
    
    def push(self, x: int) -> None:
        if(len(self.stack)<self.maxSize):
            self.stack.append(x)
        return self.stack
        
    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.stack))): 
                self.stack[i]+=val
        return self.stack
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)