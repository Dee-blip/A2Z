class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        
        def dfs(node,visited,stack):
            visited[node]=1
            
            for neighbour in adj[node]:
                if visited[neighbour]==0:
                    dfs(neighbour,visited,stack)
            stack.append(node)
                    
        
        visited=[0]*len(adj)
        stack = []
        
        for i in range(len(adj)):
            if visited[i]==0:
                dfs(i,visited,stack)
                
        return stack[::-1]
