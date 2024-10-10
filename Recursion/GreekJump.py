#https://www.geeksforgeeks.org/problems/geek-jump/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=geek-jump
class Solution:
    def minimumEnergy(self, height, n):
        
        def helper(i):
            if i==0:
                return 0
            
            left = helper(i-1) + abs(height[i] -  height[i-1])
            right = float('inf')
            if i>1:
                right = helper(i-2) + abs(height[i] -  height[i-2])
            
            return min(left,right)

            
            
        return helper(n-1)
