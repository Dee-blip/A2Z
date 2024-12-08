import heapq
class Solution:
    def nearlySorted(self, arr, k):
        
        min_heap_track = []
    
        index = 0

        for num in arr:
            heapq.heappush(min_heap_track,num)
            
            if len(min_heap_track)>k:
                arr[index] = heapq.heappop(min_heap_track)
                index+=1
                
        while len(min_heap_track):
            arr[index] = heapq.heappop(min_heap_track)
            index+=1            
        return arr
