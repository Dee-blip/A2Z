#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=sum(cardPoints[0:k])
        res=sum(cardPoints[0:k])

        rsum=0
        rindex=len(cardPoints)-1
        while k>0:
            lsum-=cardPoints[k-1]
            rsum+=cardPoints[rindex]
            res=max(res,lsum+rsum)
            k-=1
            rindex-=1

        return res



        
