from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    visited = [False] * V
	    
	    def dfs(v,parent):
	        visited[v] = True
	        
	        for neighbour in adj[v]:
	            if not visited[neighbour]:
	                if dfs(neighbour,v):
	                    return True
                elif parent!=neighbour:
                    return True
            return False
		
		
		for i in range(V):
		    if not visited[i]:
		        if dfs(i,-1):
		            return True
        return False
