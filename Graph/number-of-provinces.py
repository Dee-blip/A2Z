class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n=len(isConnected)
        m=len(isConnected[0])
        res=0
        lstmatrix = [[] for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i!=j and isConnected[i][j]==1:
                    lstmatrix[i].append(j)

        visited = [False for i in range(n)]

        def dfs(node):

            for i in lstmatrix[node]:
                if visited[i]==False:
                    visited[i] = True
                    dfs(i)

        for i in range(n):
            if visited[i]==False:
                visited[i] = True
                res+=1
                dfs(i)

        return res
