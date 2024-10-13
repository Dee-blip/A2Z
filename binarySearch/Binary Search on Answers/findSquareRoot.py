#https://www.naukri.com/code360/problems/square-root-integral_893351?leftPanelTab=0%3Futm_source%3Dstriver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
#https://www.geeksforgeeks.org/problems/square-root/0?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=square-root
import math
def floorSqrt(n):
   # Simple Approach - O(1)
   # return int(math.sqrt(n))
   #i*i<=n then its our answer

   # binary search
   low=1
   high=n
   ans=n

   while low<=high:
      mid=(low+high)//2

      if mid*mid>n:
         high=mid-1
      else:
         ans=mid 
         low=mid+1
   return ans
   
n= int(input())
print(floorSqrt(n))
