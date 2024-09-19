class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:  
        return self.helper(nums,k) - self.helper(nums,k-1)
    def helper(self,nums,k):
        count=0
        i=0
        j=0
        arr=[]
        n=len(nums)
        tempk=0
        while j<n:
            if nums[j]%2==1:
                tempk+=1  

            if tempk>k:
                while tempk>k:
                    if nums[i]%2!=0:
                        tempk-=1
                    i+=1
                

            count+=j-i+1
            j+=1
        return count
            
