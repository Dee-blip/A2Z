import heapq,math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        max_heap = []

        for i,j in points:
            heapq.heappush(max_heap,(-math.sqrt(i**2 + j**2),(i,j)))

            while len(max_heap) > k:
                heapq.heappop(max_heap)

        ans = []

        for i in range(k):
            ans.append(max_heap[i][1])
            
        return ans

