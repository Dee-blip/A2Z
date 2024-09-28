
class Solution:

    def calculateSpan(self,a,n):
        span=[int(0) for i in range(n)]
        span[0]=1
        stack=[]
        stack.append(0)
        for i in range(1,n):
            
            while len(stack)>0 and a[stack[-1]]<=a[i]:
                stack.pop()
            
            if len(stack)==0:
                span[i]=i+1
            else:
                span[i]=i-stack[-1]
            stack.append(i)
        return span

class StockSpanner:
    def __init__(self):
   
        self.st = []

    def next(self, price: int) -> int:
        span = 1  
        
        while self.st and self.st[-1][0] <= price:
            span += self.st.pop()[1] 
        
        self.st.append((price, span))
        
        return span
        
