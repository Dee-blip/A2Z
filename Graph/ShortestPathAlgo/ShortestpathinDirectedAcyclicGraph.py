from typing import List
from collections import defaultdict

class Solution:
    
    def shortestPath(self, V: int, E: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
        
        visited = [False] * V
        stack = []
        
        def dfs(node, visited, stack):
            visited[node] = True
            for neighbour, weight in adj[node]:
                if not visited[neighbour]:
                    dfs(neighbour, visited, stack)
            stack.append(node)
        
        for i in range(V):
            if not visited[i]:
                dfs(i, visited, stack)
        
        distance = [-1] * V
        distance[0] = 0  
        
        while stack:
            node = stack.pop()
            
            if distance[node] != -1:  
                for neighbour, weight in adj[node]:
                    if distance[neighbour] == -1 or distance[node] + weight < distance[neighbour]:
                        distance[neighbour] = distance[node] + weight
        
        return distance
