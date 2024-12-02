from typing import List
from collections import deque
class Solution:
    
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        if source == destination:
            return 0
        
        directions = [(-1,0),(0,-1),(0,1),(1,0)]
        
        
        queue = deque([(source[0], source[1])])
        
        distance = [[-1 for _ in range(m)] for _ in range(n)]
        distance[source[0]][source[1]] = 0
        
        while queue:
            x , y = queue.popleft()
            
                
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]==1 and distance[nx][ny]==-1:
                    distance[nx][ny] = distance[x][y]+1
                    queue.append((nx,ny))
                    
                    
                    if (nx,ny) == (destination[0],destination[1]):
                        return distance[nx][ny]
        return -1
