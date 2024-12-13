#here we need to maintain the max-heap and min-heap and make sure max_heap should have greater number of elements
import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        
        #suppose 9>10 this test is considered but if max_heap[0] contained 10 and min_heap[0] contained 9 that is incorrect statement in this case
        if self.minheap and self.maxheap and -self.maxheap[0] > self.minheap[0]:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))


        #Ensure that max_heap should haeve at most 1 more element than min_heap
        if len(self.maxheap) > len(self.minheap) +1:
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        elif len(self.maxheap) < len(self.minheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        # print(self.maxheap)
        # print(self.minheap)
        if len(self.maxheap) > len(self.minheap):
            return -self.maxheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0]) /2.0

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
