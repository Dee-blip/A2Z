# https://www.naukri.com/code360/problems/lower-bound_8165382?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION
def lowerBound(arr: [int], n: int, x: int) -> int:
    
    low=0
    high=n-1
    ans=n
    
    while low<=high:    
        mid=(low+high)//2
        if(arr[mid]>=x):
            ans=mid
            high=mid-1

        else:
            low=mid+1


    return ans    
