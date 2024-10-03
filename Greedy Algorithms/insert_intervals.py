https://leetcode.com/problems/insert-interval/description/
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=len(intervals)
        ans=[]
        i=0
        # Left side of the interval + non overlapping interval
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1

        while i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(intervals[i][0],newInterval[0])
            newInterval[1] = max(intervals[i][1],newInterval[1])
            i+=1
        ans.append(newInterval)

        while i<n:
            ans.append(intervals[i])
            i+=1
        
        return ans

        

        
