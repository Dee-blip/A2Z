#https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, w,arr,n):
        arr.sort(key=lambda x:x.value/x.weight, reverse=True)
        total_value=0.0
        
        for item in arr:
            if w<=0:
                break
            if item.weight<=w:
                total_value+=item.value
                w-=item.weight
            else:
                total_value+=(item.value/item.weight)*w
                w=0
                
        return total_value
                
