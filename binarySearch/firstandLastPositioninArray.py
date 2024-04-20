#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        res[0]=self.lowerbound(nums,target)
        res[1]=self.upperbound(nums,target)
        # to check whether target value is present in the array or not
        if(res[0]==len(nums) or nums[res[0]]!=target):
            return [-1,-1]

        return res

    
    def lowerbound(self,nums,target):
        low=0
        high=len(nums)-1
        ans=len(nums)

        while low<=high:
            mid=(low+high)//2

            if nums[mid]>=target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
    
    def upperbound(self,nums,target):
        low=0
        high=len(nums)-1
        ans=len(nums)

        while low<=high:
            mid=(low+high)//2

            if nums[mid]>target:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans-1

    




        
