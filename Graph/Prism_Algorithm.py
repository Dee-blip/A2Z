import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        
        min_heap = []
        
        visited = [False] * V
        
        heapq.heappush(min_heap,(0,0,-1))
        
        mst_sum = 0
        mst_edges = []
        
        while min_heap:
            weight,current,parent= heapq.heappop(min_heap)
            
            if visited[current]:
                continue
            
            mst_sum += weight
            visited[current] = True
            
            if parent != -1:
                mst_edges.append((parent,current,weight))
                
            for neighbour in adj[current]:
                next_vertex, edge_weight = neighbour
                
                if not visited[next_vertex]:
                    heapq.heappush(min_heap,(edge_weight,next_vertex,current))
                    
        return mst_sum

