import heapq,math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]

        heapq.heapify(max_heap)

        # print(heapq.heappop(max_heap))

        for _ in range(k):
            largest = -heapq.heappop(max_heap)

            remaining_gifts = int(math.sqrt(largest))

            heapq.heappush(max_heap,-remaining_gifts) #push the number in negative form as we using max_heap

        return -sum(max_heap)

            

            
        
