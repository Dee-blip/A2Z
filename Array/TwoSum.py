class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Optimized Approach
        d={}

        for i,j in enumerate(nums):
            check= target -j
            if check in d:
                return [i,d[check]]
            d[j]=i

        #brute force approach  
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] +nums[j]==target:
        #             return [i,j]
        
        
