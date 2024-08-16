#https://leetcode.com/problems/valid-anagram/submissions/1358107059/
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
