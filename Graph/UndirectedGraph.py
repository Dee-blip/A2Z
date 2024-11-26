from typing import List
from collections import deque

class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited = [False] * V
        
        def bfs(start):
            queue = deque([(start, -1)])  # Queue stores (node, parent)
            visited[start] = True
            
            while queue:
                node, parent = queue.popleft()
                
                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        queue.append((neighbour, node))
                    elif neighbour != parent:
                        return True
            return False
        
        # Loop through all nodes to handle disconnected components
        for i in range(V):
            if not visited[i]:
                if bfs(i):
                    return True
        return False
