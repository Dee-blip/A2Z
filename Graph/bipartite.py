class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        vis = [-1 for _ in range(n)]

        def dfs(node,c):
            vis[node] = c
            for neighbour in graph[node]:
                if vis[neighbour] == -1:
                    if dfs(neighbour,1-c)==False:
                        return False
                elif vis[neighbour] == c:
                    return False
            return True


        for i in range(n):
            if vis[i]==-1:
                if dfs(i,0)==False:
                    return False

        return True
