from collections import deque
class Solution:
    def shortestPath(self, edges, n, m, src):
        #build the adjaceny list
        #use bfs method
        
        adj = [[] for _ in range(n)]
        
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        distance = [-1 for _ in range(n)]
        distance[src] = 0
        
        queue = deque([src])
        
        while queue:
            node = queue.popleft()
            
            for neighbour in adj[node]:
                if distance[neighbour]==-1:
                    distance[neighbour] = distance[node]+1 #remind this thing we have to update the neighbour node
                    queue.append(neighbour)
                    
        return distance
