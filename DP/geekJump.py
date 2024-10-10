#https://www.geeksforgeeks.org/problems/geek-jump/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geek-jump
class Solution:
    def minimumEnergy(self, height, n):
        dp=[-1 for i in range(n)]
        
        def helper(i):
            if i==0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            
            left = helper(i-1) + abs(height[i] -  height[i-1])
            
            right = float('inf')
            if i>1:
                right = helper(i-2) + abs(height[i] -  height[i-2])
                
            dp[i]=min(left,right)
            
            return dp[i]

            

        return helper(n-1)
