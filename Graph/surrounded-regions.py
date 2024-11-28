class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])
        
        def dfs(x,y):
            if x<0 or y<0 or x>=rows or y>=cols or board[x][y]!= 'O':
                return
            board[x][y] = 'T'
            for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                dfs(x+dx,y+dy)

        
        #step-1 mark all border connected '0's as 'T'

        for i in range(rows):
            if board[i][0]== 'O':
                dfs(i,0)
            if board[i][cols-1]== 'O':
                dfs(i,cols-1)
        
        for j in range(cols):
            if board[0][j]== 'O':
                dfs(0,j)
            if board[rows-1][j]== 'O':
                dfs(rows-1,j)

        # Step 2: Flip remaining 'O' to 'X', and 'T' back to 'O'

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'


        
        
