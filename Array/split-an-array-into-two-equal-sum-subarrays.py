class Solution:
    def canSplit(self, arr):
        total_Sum = sum(arr)
        
        if total_Sum % 2 != 0:
            return False
        
        target = total_Sum //2
        running_Sum = 0
        
        for num in arr:
            running_Sum += num
            
            if running_Sum == target:
                return True
                
        return False
