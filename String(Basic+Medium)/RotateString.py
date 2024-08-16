#https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s+s
        # for i in range(len(s)):
        #     print(s[i:] + s[:i])
        #     if s[i:] + s[:i] ==goal:
        #         return True

        # return False

        
