class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0

        res=nums[0]

        for i in nums:
            currSum+=i

            res=max(res,currSum)

            if currSum<0:
                currSum=0
        return res       
