
from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        if start ==end:
            return 0
        mod = 100000
        n = len(arr)
        
        dist = [float('inf')] * mod
        dist[start] = 0
        
        queue = deque([(start,0)])
        
        
        while queue:
            node,steps = queue.popleft()
            
            for i in range(n):
                num = (arr[i]*node) % mod
                
                if steps + 1 < dist[num]:
                    dist[num] = steps +1
                    if num == end:
                        return steps+1
                    queue.append((num,steps+1))
                        
        return -1
