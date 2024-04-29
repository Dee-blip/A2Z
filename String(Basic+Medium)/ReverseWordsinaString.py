#https://leetcode.com/problems/reverse-words-in-a-string/
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])
        # split - is used to convert into string - list
        # strip -used to remove the spaces
        # join - used to rejoin t
        #  print(s.split()[::-1])
        
