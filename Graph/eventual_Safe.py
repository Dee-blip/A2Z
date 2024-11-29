class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        visited = [0] * n

        def dfs(node):
            if visited[node]!=0:
                return visited[node]
            visited[node]=1

            for neighbour in graph[node]:
                if dfs(neighbour)==1:
                    visited[node]=1
                    return 1
            visited[node]=2
            return 2

        for i in range(n):
            if visited[i]==False:
                dfs(i)
        
        return [i for i in range(n) if visited[i]==2]
