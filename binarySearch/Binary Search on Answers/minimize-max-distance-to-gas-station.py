#https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

class Solution:
    
    def check(self,stations, k, mid):
        count = 0
        n = len(stations)
        
        for i in range(1, n):
            diff = stations[i] - stations[i - 1]
            if diff > mid:
                count += diff // mid
        
        if count > k:
            return False
        else:
            return True

    def findSmallestMaxDist(self,stations, k):
        lo = 0
        n = len(stations)
        hi = stations[n - 1] - stations[0]
        
        ans = 0
        
        while lo < hi:
            mid = (lo + hi) / 2
            
            if self.check(stations, k, mid):
                ans = mid
                # to get narrow down the search space that is slightly less than the mid.
                hi = mid - 0.0001
            else:
                lo = mid + 0.0001
        
        return ans
