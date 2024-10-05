#User function Template for python3
#https://www.geeksforgeeks.org/problems/reverse-a-stack/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reverse-a-stack
from typing import List

class Solution:
    def reverse(self,St):
        n=len(St)
        return self.reverseArrayHelper(St,i=0,j=n-1)
    def reverseArrayHelper(self,St,i,j):
        if i>=j:
            return St
        
        St[i],St[j]=St[j],St[i]
        
        partial= self.reverseArrayHelper(St,i+1,j-1)
        
        return St
