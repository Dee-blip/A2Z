#https://www.naukri.com/code360/problems/aggressive-cows_1082559?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
def aggressiveCows(stalls, k):
    stalls.sort()
    low=1
    n=len(stalls)
    high=stalls[n-1]-stalls[0]
    ans=0

    while low<=high:
        mid=(low+high)//2

        if canWePlace(stalls,mid,k)==True:
            low=mid+1
            ans=mid
        else:
            high=mid-1
    return ans

def canWePlace(stalls,mid,k):
    count=1
    last=stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i]-last>=mid:
            count+=1
            last=stalls[i]
        if  count==k:
            return True
    return False



