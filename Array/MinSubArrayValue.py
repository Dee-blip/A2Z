#https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays
class Solution:
    def pairWithMaxSum(self, arr):
        
        currSum=arr[0]
        res=arr[0]
        i=0
        j=i+1
        
        while j<len(arr):
            currSum+=arr[j]
            res=max(res,currSum)
            currSum-=arr[i]
            i+=1
            j+=1
        return res
    
