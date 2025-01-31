class Solution:
    def knapSack(self, capacity, val, wt):
        
        n = len(wt)
        # v = len(val)
        memo = {}
        
        return self.knapsackRecursive(capacity,val,wt,n-1,memo)
    
    def knapsackRecursive(self,capacity,val,wt,index,memo):
        if index < 0 or capacity == 0:
            return 0
        
        if (index,capacity) in memo:
            return memo[(index,capacity)]
    
        not_take = self.knapsackRecursive(capacity,val,wt,index-1,memo)
        
        take = 0
        
        if capacity >= wt[index]:
            take = val[index] + self.knapsackRecursive(capacity - wt[index],val,wt,index-1,memo)
            
        memo[(index,capacity)] = max(take,not_take)
    
        return memo[(index,capacity)]
