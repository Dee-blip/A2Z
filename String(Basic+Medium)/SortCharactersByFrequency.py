#https://leetcode.com/problems/sort-characters-by-frequency/description/
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        a=Counter(s).most_common()##sort the dict in the decreasing order based on the frequency

        ans=""
        for i,j in a:
            ans+=i*j
        return ans
