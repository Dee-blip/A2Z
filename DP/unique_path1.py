class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(x,y):
            if x == m-1 and y == n-1:
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            
            paths = 0
            if x+1 < m:
                paths += helper(x+1,y)
            if y+1 < n:
                paths += helper(x,y+1)
            memo[(x,y)] = paths
            return paths

        return helper(0,0)
