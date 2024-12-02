from heapq import heappop, heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adj = defaultdict(list)

        for x,y,cost in flights:
            adj[x].append((y,cost))

        pq = []

        heappush(pq,(0,src,k+1))

        visited = {}

        while pq:
            cost,city,stops = heappop(pq)

            if city == dst:
                return cost
            
            if stops>0:
                for neighbour, price in adj[city]:
                    new_cost = cost + price

                    if(neighbour,stops-1) not in visited or new_cost < visited[neighbour,stops-1]:
                        visited[(neighbour,stops-1)] = new_cost
                        heappush(pq,(new_cost,neighbour,stops-1))

        return -1
        
