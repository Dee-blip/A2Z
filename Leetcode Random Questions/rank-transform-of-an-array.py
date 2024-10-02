#https://leetcode.com/problems/rank-transform-of-an-array/description/
from collections import Counter
import copy
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
    
        sortedArr = copy.deepcopy(list(set(arr)))
        sortedArr.sort()
        d={}
        for i in range(len(sortedArr)):
            d[sortedArr[i]]= i
        ans=[]
        # d = dict(sorted(d.items(), key=lambda item: item[1]))
        for i in arr:
            ans.append(d[i]+1)
        return ans
        



        
