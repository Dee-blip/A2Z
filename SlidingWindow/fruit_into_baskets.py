class Solution:
    def totalFruits(self,arr):
        k=2
        
        i=0
        j=0
        
        d={}
        res=0
        while j<len(arr):
            if arr[j] in d:
                d[arr[j]]+=1
            else:
                d[arr[j]]=1
            
            
            while len(d)>k:
                d[arr[i]]-=1
      
                if  d[arr[i]]==0:
                    d.pop(arr[i])
                i+=1
                    

            res=max(res,j-i+1)
            j+=1
        
        return res
            
