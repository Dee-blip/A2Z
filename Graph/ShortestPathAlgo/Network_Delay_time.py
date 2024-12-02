from collections import defaultdict
from heapq import heappop,heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #create the adjacent list
        adj= defaultdict(list)
        
        for u,v,w in times:
            adj[u].append((v,w))

        distance = [float('inf')] * (n+1)
        distance[k] = 0

        pq = []
        heappush(pq,(0,k))

        while pq:
            dist , node = heappop(pq)

            for neighbour,travel_time in adj[node]:
                if dist + travel_time < distance[neighbour]:
                    distance[neighbour] = dist + travel_time
                    heappush(pq,(distance[neighbour], neighbour))

        max_distance = max(distance[1:])
        return -1 if max_distance == float('inf') else max_distance

