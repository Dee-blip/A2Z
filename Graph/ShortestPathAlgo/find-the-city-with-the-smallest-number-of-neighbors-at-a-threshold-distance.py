class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != float('inf') and dist[j][k] != float('inf'):
                        dist[i][j] = min(dist[j][i],dist[i][k]+dist[k][j])

        reachable_count_dic = {}

        for i in range(n):
            reachable_count = 0
            for j in range(n):
                if i!=j:
                    if dist[i][j]<=distanceThreshold:
                        reachable_count+=1

            reachable_count_dic[i] = reachable_count

        min_count = float('inf')
        result_city = -1
    
        for city,count in reachable_count_dic.items():
            if count<min_count or (count == min_count and city>result_city):
                min_count = count
                result_city = city
        return result_city
