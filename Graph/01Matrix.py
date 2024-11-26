from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()

        result = [[-1]* cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    result[i][j]=0

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions:
                nr,nc=r+dr,c+dc

                if 0<=nr<rows and 0<=nc<cols:
                    if result[nr][nc]==-1:
                        result[nr][nc]= result[r][c]+1
                        queue.append((nr,nc))

        return result
