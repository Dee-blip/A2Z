class Solution:
  def search(self, nums: List[int], target: int) -> int:
      low=0
      high=len(nums)-1
      return self.findsearch(nums,target,low,high)
  def findsearch(self,nums,target,low,high):
      if low>high:
          return -1
      n=len(nums)
      mid=low+(high-low)//2
      
      if nums[mid]==target:
          return mid
      elif nums[mid]>target:
          return self.findsearch(nums,target,low,mid-1)
      else:
          return self.findsearch(nums,target,mid+1,high)
