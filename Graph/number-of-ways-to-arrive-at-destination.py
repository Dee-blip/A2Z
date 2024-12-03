from heapq import heappop,heappush

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))

        dist = [float('inf')] * n
        ways = [0]*n

        dist[0] = 0
        ways[0] = 1

        min_heap = [(0,0)]
        mod = int(1e9+7)
        
        while min_heap:
            dis,node = heappop(min_heap)

            for adjNode, time_taken in adj[node]:
                if dis + time_taken < dist[adjNode]:
                    dist[adjNode]  = dis + time_taken
                    heappush(min_heap,(dist[adjNode],adjNode))
                    ways[adjNode] = ways[node]
                elif dis + time_taken == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode]+ways[node]) % mod
        return ways[n-1]



        

        
