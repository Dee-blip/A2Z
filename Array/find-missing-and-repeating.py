from collections import Counter
class Solution:
    def findTwoElement( self,arr, n):
        ans=[]
        dict1=Counter(arr)
        for i, j in  dict1.items():
            if j==2:
                ans.append(i)
                break
        X=1
        arr.sort()
        for i in range(n):
            if arr[i]==X:
                X+=1
                
        ans.append(X)
        return ans
            
        
        # code here
