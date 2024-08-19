#https://leetcode.com/problems/sliding-window-maximum/description/
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        j=0
        n=len(nums)
        q = deque()
        arr=[]
        maxtemp=0

        while j<n:
            while q and q[-1]<nums[j]:
                q.pop()
            q.append(nums[j])

            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                arr.append(q[0])
     
                if q[0]==nums[i]:
                    q.popleft()
                i+=1
                j+=1
        return arr

        # if len(nums)==1 and k==1:
        #     return nums
        # i=0
        # j=0
        # n=len(nums)
        # res=[]
        # max1=0
        # tempmax=-99999

        # while j<n:
        #     if nums[j]>tempmax:
        #         tempmax= nums[j]
            
        #     if j-i+1<k:
        #         j+=1
        #     elif j-i+1==k:
        #         res.append(tempmax)
        #         i+=1
        #         tempmax=nums[i]
        #         if nums[j]>tempmax:
        #             tempmax=nums[j]
        #         j+=1
        # return res


        #Need to Optimized the code
        # i=0
        # j=0
        # n=len(nums)
        # temp=[]
        # res=[]
        # while j<n:
        #     temp.append(nums[j])

        #     if j-i+1<k:
        #         j+=1
        #     elif j-i+1==k:
        #         max1=max(temp)
        #         res.append(max1)
        #         temp.pop(0)
        #         i+=1
        #         j+=1
        # return res
        

        
