from typing import List

class Solution:
    def topoSort(self,V,adj):
        
        def dfs(node,visited,stack):
            visited[node] = 1
            
            for neighbour in adj[node]:
                if visited[neighbour]==0:
                    dfs(neighbour,visited,stack)
            stack.append(node)
        
        visited = [0]*V
        stack = []
        
        for i in range(V):
            if visited[i]==0:
                dfs(i,visited,stack)
                
        return stack[::-1]
    
    def findOrder(self, dict, k):
        N = len(dict)
        adj = [[] for _ in range(k)]
        
        for i in range(N-1):
            s1 = dict[i]
            s2 = dict[i+1]
            
            min_len = min(len(s1),len(s2))
            
            for j in range(min_len):
                if s1[j] != s2[j]:
                    adj[ord(s1[j]) - ord('a')].append(ord(s2[j]) - ord('a'))
                    break
                
        topo = self.topoSort(k,adj)
        
        ans=""
        for char in topo:
            ans+= chr(char + ord('a'))
            
        return ans
