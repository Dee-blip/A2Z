from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows,cols = len(heights),len(heights[0])

        effort = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        effort[0][0] = 0

        min_heap = [(0,0,0)]

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        while min_heap:
            current_effort,r,c = heappop(min_heap)

            if r==rows-1 and c == cols-1:
                return current_effort

            for x,y in directions:
                nx,ny = r+x,y+c

                if 0<=nx<rows and 0<=ny<cols:
                    new_effort = max(current_effort,abs(heights[nx][ny]-heights[r][c]))

                    if new_effort < effort[nx][ny]:
                        effort[nx][ny] = new_effort
                        heappush(min_heap,(new_effort,nx,ny))

        return -1




        
