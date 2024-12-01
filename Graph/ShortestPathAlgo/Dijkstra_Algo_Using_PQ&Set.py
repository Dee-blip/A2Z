from heapq import heappop,heappush
class Solution:
    # Function to find the shortest distance of all the vertices
    # from the source vertex src.
    #using PQ
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        # pq=[]
        
        # heappush(pq,(0,src))
        
        # distance = [float('inf')] * V
        # distance[src] = 0
        
        
        # while pq:
        #     dist,node = heappop(pq)
            
        #     for neighbour,weight in adj[node]:
        #         if dist + weight < distance[neighbour]:
        #             distance[neighbour] = dist + weight
        #             heappush(pq,(distance[neighbour],neighbour))
                    
        # return [d if d!=float('inf') else -1 for d in distance]
        
        
        #using set
        
        distance = [float('inf')] * len(adj)
        distance[src] = 0
        
        active_nodes = set()
        active_nodes.add((0,src))
        
        
        while active_nodes:
            dist,node = min(active_nodes)
            active_nodes.remove((dist,node))
            
            for neighbour,weight in adj[node]:
                if dist + weight < distance[neighbour]:
                    distance[neighbour] = dist + weight
                    active_nodes.add((distance[neighbour],neighbour))
        return [d if d!=float('inf') else -1 for d in distance]
