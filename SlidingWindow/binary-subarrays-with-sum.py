#https://leetcode.com/problems/binary-subarrays-with-sum/
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.getCount(nums,goal) - self.getCount(nums,goal-1)
    
    def getCount(self,nums,goal):
        if goal<0:
            return 0
        l=0
        r=0
        count=0
        sum1=0
        n=len(nums)
        while r<n:
            sum1+=nums[r]
            while sum1>goal:
                sum1-=nums[l]
                l+=1
            count+=(r-l)+1
            r+=1
        return count
                

        
        
