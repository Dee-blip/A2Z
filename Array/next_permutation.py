class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)
        i = n-2

        #find the smaller number to the right starting from the right - first decreasing element
        while i>=0 and nums[i] >= nums[i+1]:
            i-=1

        #if there is i exist and next step is to find the next just greater element and swap it
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            
            nums[i],nums[j] = nums[j],nums[i]

        #swap it
        nums[i+1:] = reversed(nums[i+1:])
        
