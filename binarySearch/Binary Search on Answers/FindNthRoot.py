#https://www.naukri.com/code360/problems/nth-root-of-m_1062679?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
import math
def NthRoot(n: int, m: int) -> int:
    low=1
    high=m
    ans=-1
    while low<=high:
        mid=(low+high)//2
        check=math.pow(mid,n)
        if check==m:
            return mid
            break

        elif check>m:
            high=mid-1

        else:
            low=mid+1
        
    return ans

        
