class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[]
        right = [0] * n
        res=0

        for i in range(n):
            if i==0:
                left.append(height[i])
            else:
                left.append(max(left[-1],height[i]))
    

        for i in range(n-1,-1,-1):
            if i==n-1:
                right[i]=height[i]
            else:
                right[i]=max(right[i+1],height[i])

        for i in range(n):
            res+=min(left[i],right[i]) - height[i]
        return res
        
