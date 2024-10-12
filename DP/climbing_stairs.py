#-https://leetcode.com/problems/climbing-stairs/description/
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[-1 for i in range(n+1)]
        return self.helper(n,dp) 
    # 1-step = from n-1 to n
    # 2-step = from n-2 to n
    def helper(self,n,dp):
            if n<=1:
                return 1
            if dp[n]!=-1:
                return dp[n]
            dp[n]= self.helper(n-1,dp) + self.helper(n-2,dp)
            return dp[n]

        
