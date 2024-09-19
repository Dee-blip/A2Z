class Solution:

    def helper(self,nums,k):
        d={}
        i=0
        j=0
        res=0
        while j<len(nums):
            if nums[j] in d:
                d[nums[j]]+=1
            else:
                 d[nums[j]]=1

            if len(d)>k:
                while len(d)>k:
                    d[nums[i]]-=1
                    if d[nums[i]]==0:
                        d.pop(nums[i])
                    i+=1
            if (len(d)<=k):       
                res+=(j-i+1)

            j+=1
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums,k) - self.helper(nums,k-1)    
        

        
