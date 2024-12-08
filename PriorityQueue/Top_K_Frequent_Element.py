import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        
        max_heap = []
        for num,freq in dic.items():
            heapq.heappush(max_heap,(-freq,num))

        ans=[]
        
        for i in range(k):
            ans.append(heapq.heappop(max_heap)[1])
        return ansxa


        

    
        
