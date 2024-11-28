from collections import deque
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topologicalSort(self,adj):
        rows=len(adj)
        cols= len(adj[0])
        #step1 Store the degree for each node
        in_degree = [0] * rows
        
        for i in range(rows):
            for j in adj[i]:
                in_degree[j]+=1
                
            
        queue = deque()
        
        for i in range(rows):
            if in_degree[i]==0:
                queue.append(i)
                
        
        topo_order = []
        
        while queue:
            u = queue.popleft()
            
            topo_order.append(u)
            
            for v in adj[u]:
                in_degree[v]-=1
                
                if in_degree[v]==0:
                    queue.append(v)
                    
        if len(topo_order) == rows:
            return topo_order
        else:
            return []
