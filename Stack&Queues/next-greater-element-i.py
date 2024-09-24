class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        n=len(nums2)
        ans=[]

        d={}
        d1={}

        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums2[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
                d1[nums2[i]]=-1
            else:        
                ans.append(stack[-1])
                d1[nums2[i]]= stack[-1]
            stack.append(nums2[i])

        return [d1[i] for i in nums1]
        


        
