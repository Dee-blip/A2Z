#https://leetcode.com/problems/lemonade-change/
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten = 0

        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                if five>0:
                    five-=1
                    ten+=1
                else:
                    return False
            else:
                if(ten and five):
                    ten-=1
                    five-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
        
