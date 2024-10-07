#-https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07
class Solution:
    def minLength(self, s: str) -> int:
        stack=[]

        for i in s:
            if stack and ((stack[-1]=='A' and i=='B') or (stack[-1]=='C' and i=='D')):
                stack.pop()
            else:
                stack.append(i)
        return len(stack)
        
