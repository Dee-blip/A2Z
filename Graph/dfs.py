class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        
        def dfs(node):
            visited[node] = True
            result.append(node)
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour)
            
            
        
        visited = [False] * len(adj)
        result = []
        
        dfs(0)
        
        
        
        return result
            
