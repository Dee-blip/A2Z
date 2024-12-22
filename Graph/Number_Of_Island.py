class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])


        def marked_other(i,j):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]=="0":
                return

            grid[i][j] = "0"

            marked_other(i,j-1)
            marked_other(i,j+1)
            marked_other(i-1,j)
            marked_other(i+1,j)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    res+=1
                    marked_other(i,j)
        return res
