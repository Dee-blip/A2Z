import heapq
class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        max_heap = []
        
        for num in A:
            heapq.heappush(max_heap,-num)
            
            while len(max_heap)>K2:
                heapq.heappop(max_heap)
        
        sorted_negative = [-num for num in max_heap]        
        sorted_list = sorted(sorted_negative)
    
        
        return sum(sorted_list[K1:K2-1])
