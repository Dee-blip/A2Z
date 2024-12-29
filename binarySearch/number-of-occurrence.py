class Solution:
    def countFreq(self, arr, target):
        
        index  = self.binarySearch(arr,target)
        
        if index == -1:
            return 0
        
        upper = self.upperBound(arr,target)
        
        return upper - index +1
        
    def binarySearch(self,arr,target):
        n = len(arr)
        
        l = 0
        h = n -1
        
        ans = -1
        
        while l <=h:
            mid = (l+h)//2
            if arr[mid] >= target:
                ans = mid
                h = mid - 1
            else:
                l = mid + 1
                
        return ans
        
    def upperBound(self,arr,target):
        n = len(arr)
        
        l = 0
        h = n -1
        ans = -1
        
        while l <=h:
            mid = (l+h)//2
            
            if arr[mid] <=  target:
                l = mid + 1
                ans = mid
            else:
                h = mid -1
                
        return ans
