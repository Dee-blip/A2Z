from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        max_difference = -1 
        min_ele = nums[0]   
        for num in nums[1:]: 
            if num  > max_difference:  
                max_difference = max(max_difference, num - min_ele)

            if num < min_ele:  
                min_ele = num

        return max_difference
