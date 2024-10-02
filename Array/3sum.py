class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=[]

        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j=i+1
            k=n-1

            while j<k:
                temp = nums[i]+nums[j]+nums[k]

                if temp==0:
                    if ([nums[i],nums[j],nums[k]]) not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif temp>0:
                    k-=1
                else:
                    j+=1
        return res






        
