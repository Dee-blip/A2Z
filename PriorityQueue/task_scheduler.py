from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)

        max_heap = [-count for count in task_counts.values()]

        heapq.heapify(max_heap)
        time = 0

        while max_heap:
            temp=[]

            for _ in range(n+1):
                if max_heap:
                    temp.append(heapq.heappop(max_heap))
                    
            for t in temp:
                if t+1<0:
                    heapq.heappush(max_heap,t+1)

            if max_heap:
                time+= (n+1)
            else:
                time+=len(temp)

        return time
        
