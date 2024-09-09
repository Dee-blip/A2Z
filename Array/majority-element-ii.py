class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[]
        d={}
        for i in nums:
            if i in d:
                d[i]+=1

            else:
                d[i]=1
        # print(d)

        for i,j in d.items():
            if j>n/3:
                ans.append(i)
        return ans
                
