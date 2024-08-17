class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=[0]*n

        j=0
        k=1

        for i in range(n):
            if nums[i]<0:
                arr[k]=nums[i]
                k+=2
            else:
                arr[j]=nums[i]
                j+=2
        return arr



        
