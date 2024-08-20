class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            currentProfit = prices[i]-buy
            if currentProfit<0:
                buy=prices[i]
            profit = max(profit,currentProfit)

        return profit
         
