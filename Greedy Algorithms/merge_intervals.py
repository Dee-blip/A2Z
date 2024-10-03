#https://leetcode.com/problems/merge-intervals/description/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        n=len(intervals)
        ans=[intervals[0]]
        i=1

        while i<n:
            if ans[-1][1]>= intervals[i][0]:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])
            else:
                ans.append(intervals[i])
            i+=1

        return ans
