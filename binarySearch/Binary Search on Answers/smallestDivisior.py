https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/
import math
class Solution:
    def totalDivisor(self,nums,mid):
        totalSum=0
        for i in range(len(nums)):
            totalSum+=math.ceil(nums[i]/mid)
     
        return totalSum


    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=maxDivisor=max(nums)
        res=0

        while low<=high:
            mid=(low+high)//2

            ans=self.totalDivisor(nums,mid)

            if ans<=threshold:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res if res!=float('inf') else -1 


        

    

        
