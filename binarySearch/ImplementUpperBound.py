# https://www.naukri.com/code360/problems/implement-upper-bound_8165383?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
def upperBound(arr: [int], x: int, n: int) -> int:    
       
    low=0
    high=n-1
    ans=n
    
    while low<=high:    
        mid=(low+high)//2
        if(arr[mid]>x):
            ans=mid
            high=mid-1

        else:
            low=mid+1


    return ans    
