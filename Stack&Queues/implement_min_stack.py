#https://leetcode.com/problems/min-stack/description/
class MinStack:

    def __init__(self):
        self.stack=[[],[]]
    
    def push(self, val: int) -> None:
        self.stack[0].append(val)
        if len(self.stack[1])==0 :
            self.stack[1].append(val)
        else:
            self.stack[1].append(min(val, self.stack[1][-1]))

        return self.stack[0]

    def pop(self) -> None:
        if self.stack[0]:
            self.stack[0].pop()
            self.stack[1].pop()

    def top(self) -> int:
        return self.stack[0][-1]

    def getMin(self) -> int:
        return self.stack[1][-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
