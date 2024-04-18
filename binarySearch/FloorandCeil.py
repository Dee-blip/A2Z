#For the floor
def getFloor(a, n, x):
    low=0
    high=n-1
    ans=-1
    
    while low<=high:    
        mid=(low+high)//2

        if(arr[mid]<=mid):
            ans=a[mid]
            low=mid+1

        else:
           high=mid-1


    return ans 

def getCeil(a, n, x):
    low=0
    high=n-1
    ans=-1
    
    while low<=high:    
        mid=(low+high)//2

        if(arr[mid]>=mid):
            ans=a[mid]
           high=mid-1

        else:
           low=mid+1

    return ans 
