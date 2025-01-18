class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        memo = {}
        def helper(x,y):
            if x == n -1 and y == m-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            
            if obstacleGrid[x][y] ==1:
                return 0 
            paths = 0
            if x+1< n:
                paths += helper(x+1,y)
            if y+1< m:
                paths += helper(x,y+1)
            memo[(x,y)] = paths
            return paths 
        
        if obstacleGrid[0][0] == 1 or obstacleGrid[n-1][m-1]==1:
            return 0
        
        return helper(0,0)
        
