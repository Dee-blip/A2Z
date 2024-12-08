import heapq

class Solution:

    def kLargest(self, arr, k):
        min_heap = []
        
        for num in arr:
            heapq.heappush(min_heap, num)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return heapq.nlargest(k, min_heap)
