#https://leetcode.com/problems/koko-eating-bananas/description/
import math
class Solution:
    def totalHours(self,piles,hourly):
        totalHours=0
        for i in range(len(piles)):
            totalHours+=math.ceil(piles[i]/hourly)
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #1 to max of piles
        low=1
        high=max(piles)
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            # print(mid)
            getHourly=self.totalHours(piles,mid)

            if getHourly<=h:
                ans= mid
                high=mid-1
            else:
                low=mid+1

        return ans





