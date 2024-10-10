class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0 
        
        
        for i in range(1, n):
            # Look back at most k stones
            for j in range(max(0, i - k), i):
                cost = dp[j] + abs(arr[i] - arr[j])
                dp[i] = min(dp[i], cost)
        
        return dp[-1] 
        # code here
