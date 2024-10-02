#User function Template for python3
#https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        n=len(arr)
        arr.sort()
        dep.sort()
        count=0
        ans=0
        i,j=0,0
        
        while i<n:
            if arr[i]<=dep[j]:
                count+=1
                ans=max(ans, count)
                i+=1
            elif arr[i]>dep[j]:
                count-=1
                j+=1
                
        return ans

