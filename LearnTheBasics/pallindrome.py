#link -https://leetcode.com/problems/palindrome-number/description/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        check1=x
        check2=0

        while x>0:
            d = x%10
            check2 = (check2*10)+d
            x//=10

        if check1==check2:
            return True
        return False
        
