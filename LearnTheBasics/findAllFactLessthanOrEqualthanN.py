#User function Template for python3

class Solution:
    
    def factorial(self,N):
        if N==1:
            return 1
        return N * self.factorial(N-1)
    
    
    def factorialNumbers(self, n):
        ans=[]
        for i in range(1,n+1):
            res=self.factorial(i)
            if res>n:
                break
            ans.append(res)
        return ans
            
