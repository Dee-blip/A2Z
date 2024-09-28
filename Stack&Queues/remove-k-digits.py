class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n=len(num)
        stack=[]
        for i in range(n):
            while stack and k>0 and stack[-1]>num[i]:
                stack.pop()
                k-=1
            stack.append(num[i])
    
        while k>0 :
            stack.pop()
            k-=1
        
        res=''.join(stack).lstrip('0')

        return res if res else '0'
