#problem link  -https://leetcode.com/problems/word-search/
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # we can go in any directions here after finding the first letter of the word and also marked if you visited any char in the board . if you dont find that word then backtrack it and replace the visited char with the original word

        def backtrack(i,j,index):
            if index == len(word):
                return True
            if i<0 or j<0 or i>=n or j>=m or board[i][j] != word[index]:
                return False
            temp = board[i][j]
            board[i][j] = "#"

            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            for di,dj in directions:
                if backtrack(i+di,j+dj,index+1):
                    return True
            
            board[i][j] = temp
            return False
            

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and backtrack(i,j,0):
                    return True

        return False
