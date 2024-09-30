class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []
        n=len(s)
        for i in range(n):
            if s[i]=="(":
                left.append(i)
            elif s[i]=="*":
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left:
            if not star:
                return False
            if star[-1]>left[-1]:
                left.pop()
                star.pop()
            else:
                return False
        return True
