https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
class Solution:
    def getNumberOfDays(self,bloomDay,k,mid):
        tempCount=0
        final=0
        for i in range(len(bloomDay)):
            if bloomDay[i]<=mid:
                tempCount+=1
            else:
                final+=tempCount//k
                tempCount=0
        final+=tempCount//k
        return final

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        minDays=min(bloomDay)
        maxDays=max(bloomDay)
        res=float('inf')
        while minDays<=maxDays:
            mid=(minDays+maxDays)//2
            print(mid)

            ans= self.getNumberOfDays(bloomDay,k,mid)
            print(ans)

            if ans>=m:
                res=min(res,mid)
                maxDays=mid-1
            else:
                minDays=mid+1
        return res if res!=float('inf') else -1
                
            
        
