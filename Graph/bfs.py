#User function Template for python3
from typing import List
from collections import deque
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        visited = [False] * len(adj)
        result = []
        queue = deque([0])
        
        visited[0] = True
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for neighbour in adj[current]:
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append(neighbour)
                    
        return result
