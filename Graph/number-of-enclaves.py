class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(x,y):
            if x<0 or y<0 or x>=rows or y>=cols or grid[x][y]!=1:
                return 
            grid[x][y] = 'T'

            for dx,dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(x+dx,y+dy)

        
        for i in range(rows):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][cols-1] == 1:
                dfs(i,cols-1)

        for j in range(cols):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[rows-1][j] == 1:
                dfs(rows-1,j)
        
        ans = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    ans+=1
        
        return ans
        
