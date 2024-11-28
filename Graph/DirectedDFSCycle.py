from typing import List

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        
        def dfs(node,visited,pathvisited):
            visited[node] = True
            pathvisited[node] = True
            
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    if dfs(neighbour,visited,pathvisited):
                        return True
                    
                elif pathvisited[neighbour]:
                    return True
                    
            pathvisited[node] = False
            return False
            
            
            
        visited = [False] * V
        pathvisited = [False] * V
        
        for i in range(V):
            if not visited[i]:
                if dfs(i,visited,pathvisited):
                    return True
                    
        return False

