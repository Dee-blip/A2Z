Link - https://leetcode.com/problems/longest-happy-string/
#Time Complexity - O(a+b+c)
#Space Complexity - O(a+b+c)
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []

        result = []

        if a>0:
            heapq.heappush(max_heap,(-a,'a')) #O(log3) =1
        if b>0:
            heapq.heappush(max_heap,(-b,'b'))
        if c>0:
            heapq.heappush(max_heap,(-c,'c'))

        while max_heap:
            count1,char1 = heapq.heappop(max_heap)

            if len(result)>=2 and result[-1]==result[-2] == char1:
                if not max_heap:
                    break
                count2,char2 = heapq.heappop(max_heap)
                result.append(char2)
                count2+=1
                if count2!=0:
                    heapq.heappush(max_heap,(count2,char2))
                heapq.heappush(max_heap,(count1,char1))
            else:
                result.append(char1)
                count1+=1
                if count1!=0:
                    heapq.heappush(max_heap,(count1,char1))

        return "".join(result)
                



        
        
