class Solution:

	def prevSmaller(self, A):
        stack=[]
        n=len(A)
        ans=[]
        for i in range(n):
            while len(stack)!=0 and stack[-1]>=A[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            else:
                
                ans.append(stack[-1])

            stack.append(A[i])
            
        return ans
