class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        max1=max(list(d.values()))
        # print(max1)
        
        for i,j in d.items():
            if j==max1:
                return i
            
