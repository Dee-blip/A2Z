#https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0
class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        dic={}
        
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
  
        for i in range(N):
            if i+1 in dic:
                arr[i]=dic[i+1]
            else:
                arr[i]=0
        
        return arr
