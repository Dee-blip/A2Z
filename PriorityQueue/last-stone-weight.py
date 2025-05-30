import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap,-stone)

        while len(max_heap)>1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            
            if x == y:
                continue
            if x != y:
                heapq.heappush(max_heap, x-y)

        return 0 if not max_heap else -max_heap[0]


