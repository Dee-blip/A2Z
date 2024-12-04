class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        distance = [100000000] * V
        
        distance[src] = 0
        #relaxation
        for i in range(V-1):
            for u,v,w in edges:
                if distance[u]!=100000000 and distance[u]+ w < distance[v]:
                    distance[v] = distance[u] + w
                    
        #find the negative cycle
        for u,v,w in edges:
            if distance[u]!=100000000 and distance[u] + w<distance[v]:
                return [-1]
                
                
        return distance
