##User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n1=len(arr1)
        n2=len(arr2)
        
        i=0
        j=0
        
        findCount=0
        
        while i<n1 or j<n2:
            if i<n1 and (j>=n2 or arr1[i]<=arr2[j]):
                current_ele = arr1[i]
                i+=1
            else:
                current_ele = arr2[j]
                j+=1
                
          
            if findCount ==k-1:
                return current_ele
            findCount+=1
            
        return -1
#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n1=len(arr1)
        n2=len(arr2)
        
        i=0
        j=0
        
        findCount=0
        
        while i<n1 or j<n2:
            if i<n1 and (j>=n2 or arr1[i]<=arr2[j]):
                current_ele = arr1[i]
                i+=1
            else:
                current_ele = arr2[j]
                j+=1
                
          
            if findCount ==k-1:
                return current_ele
            findCount+=1
            
        return -1
