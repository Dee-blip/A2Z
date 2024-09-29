#https://www.geeksforgeeks.org/problems/number-of-coins1824/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
	def minCoins(self, coins, M, sum):
	    coins.sort()
	    n=len(coins)
	    ans=[]
	    print(coins)
	   
	    for i in range(n-1,-1,-1):
	        while sum>=coins[i]:
	            sum-=coins[i]
	            ans.append(coins[i])
	            
	    return len(ans)
	       
