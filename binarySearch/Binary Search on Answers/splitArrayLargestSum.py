class Solution:
    def checkLengthisEqual(self,nums,check):
        painter =1
        lengthIncrement = 0

        for i in range(len(nums)):
            if lengthIncrement + nums[i] <=check:
                lengthIncrement+=nums[i]
            else:
                painter +=1
                lengthIncrement=nums[i]
        return painter

    def splitArray(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return -1

        low = max(nums)
        high = sum(nums)
        ans = float('inf')

        while low<=high:
            mid=(low+high)//2

            if self.checkLengthisEqual(nums,mid)<=k:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


        
