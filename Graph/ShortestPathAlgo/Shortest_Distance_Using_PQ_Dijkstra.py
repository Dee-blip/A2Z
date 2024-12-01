#User function Template for python3
from typing import List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Priority queue for Dijkstra's algorithm
        pq = []
        heappush(pq, (0, 1))  # (distance, node)
        
        # Distance array and parent array
        distance = [float('inf')] * (n + 1)
        distance[1] = 0
        parent = [-1] * (n + 1)
        
        while pq:
            dist, node = heappop(pq)
            
            # Process neighbors of the current node
            for neighbour, weight in adj[node]:
                if dist + weight < distance[neighbour]:
                    distance[neighbour] = dist + weight  # Corrected
                    parent[neighbour] = node
                    heappush(pq, (distance[neighbour], neighbour))
        
        # If the destination node is unreachable
        if distance[n] == float('inf'):
            return [-1]
        
        # Backtrack to reconstruct the path
        path = []
        current = n
        while current != -1:
            path.append(current)
            current = parent[current]
        
        path.reverse()
        
        return [distance[n]] + path
