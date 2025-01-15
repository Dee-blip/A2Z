https://leetcode.com/problems/longest-increasing-subsequence/description/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #brute force is get all the subsequences and check which is increase and keep maintain the longest count for those subsequences which is in increasing order
        #Optimising Approach
        #10 can be part of the LIS or not but 9 can't be part of the LIS - think about current and previous based upon previous think whether we can take that element or not - function(index,prev_index) - T(2n)

        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        return max(LIS)
