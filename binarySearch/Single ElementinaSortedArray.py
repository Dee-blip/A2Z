#https://leetcode.com/problems/single-element-in-a-sorted-array/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # if len(nums)==1:
        #     return nums[0]

        #first way to via dictionary or hasing
        #second one is iterate over the array and find the unique element - brute force approach
        # for i in range(len(nums)):
        #     if i==0:
        #         if nums[i]!=nums[i+1]:
        #             return nums[i]
        #     elif i==len(nums)-1:
        #         if nums[i-1]!=nums[i]:
        #             return nums[i]
        #     else:
        #         if (nums[i]!=nums[i-1]) and (nums[i]!=nums[i+1]):
        #             return nums[i]
            
        #binary search 

        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]

        low=1
        high=n-2

        while low<=high:
            mid=(low+high)//2

            if (nums[mid-1]!=nums[mid] and nums[mid+1]!=nums[mid]):
                return nums[mid]
            #left half - stand in even or odd index
            if(mid%2==1 and nums[mid-1]==nums[mid]) or (mid%2==0 and nums[mid+1]==nums[mid])  :
                low=mid+1
            else:
                high=mid-1 #eliminate right half
        return -1



                
        
