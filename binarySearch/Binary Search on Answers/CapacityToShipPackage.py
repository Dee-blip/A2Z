https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
class Solution:
    def getMeTheWeight(self,weights,capacity):
        tempWeightCount=0
        days=1
        for i in range(len(weights)):
            if tempWeightCount + weights[i]> capacity:
                days+=1
                tempWeightCount=weights[i]
            else:
                tempWeightCount+=weights[i]

        return days
        

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low=max(weights)
        high=sum(weights)
        print(low)
        print(high)

        ans=float('inf')
         
        while low<=high:
            mid=(low+high)//2

            noOfDays=self.getMeTheWeight(weights,mid)

            if noOfDays<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans








        
