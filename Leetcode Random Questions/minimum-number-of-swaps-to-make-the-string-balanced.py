class Solution:
    def minSwaps(self, s: str) -> int:
        # remaining=[]
        imbalance=0
        maximbalance = 0

        for i in s:
            if i =='[':
                imbalance-=1
            else:
                imbalance+=1
                maximbalance=max(maximbalance,imbalance)
        return (maximbalance+1)//2
