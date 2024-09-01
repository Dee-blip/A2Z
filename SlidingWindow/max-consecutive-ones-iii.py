class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        maxlen=0

        while j<len(nums):
            if nums[j]==0:
                k-=1
            if k<0:
                if nums[i]==0:
                    k+=1
                i+=1
       
            maxlen =max(maxlen,j-i+1)
            j+=1
        return maxlen


        # i=0
        # j=0
        # maxlen=0

        # while j<len(nums):
        #     if nums[j]==0:
        #         k-=1
        #     while k<0:
        #         if nums[i]==0:
        #             k+=1
        #         i+=1
       
        #     maxlen =max(maxlen,j-i+1)
        #     j+=1
        # return maxlen

        
