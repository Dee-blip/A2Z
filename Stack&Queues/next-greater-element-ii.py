class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        ans=[-1]*n
        d={}

        for i in range(2*n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if stack:
                    ans[i]= stack[-1]
                 
            stack.append(nums[i%n])

        return ans
        
