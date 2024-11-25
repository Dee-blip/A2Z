class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        if fresh == 0:
            return 0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        time = 0

        while q:
            size = len(q)
            
            for _ in range(size):
                i,j = q.popleft()

                for dx,dy in directions:
                    ni = i+dx
                    nj = j+dy

                    if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                        grid[ni][nj]=2
                        q.append((ni,nj))
                        fresh-=1
            if q:
                time+=1

        return -1 if fresh > 0 else time
        
