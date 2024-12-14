class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #initially approach is brute force approach and get all the pairs and check if any pair sum==k if yes increase the count
        current_Sum = 0
        count = 0

        prefix_Sum = {0:1} # Initialize with 0:1 to handle cases where current_sum == k

        for num in nums:
            current_Sum += num

            if current_Sum - k in prefix_Sum:
                count+= prefix_Sum[current_Sum - k]

            prefix_Sum[current_Sum] =  prefix_Sum.get(current_Sum,0) +1

        return count
