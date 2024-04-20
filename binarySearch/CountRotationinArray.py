#https://www.naukri.com/code360/problems/rotation_7449070?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
import sys
def findKRotation(arr : [int]) -> int:
        n=len(arr)

        low=0
        high=n-1

        ans = sys.maxsize
        while low<=high:
            mid=(low+high)//2

            if arr[low]<=arr[mid]<=arr[high]:
                if(arr[low]<ans):
                    ans=arr[low]
                    index=low
                break
            # we are here only picking the lowest from the sorted array and then eliminating the sorted array and then check in unsorted one and compare the ans to get the min value
            if arr[low]<=arr[mid]:
                if(arr[low]<ans):
                    ans=arr[low]
                    index=low
                low=mid+1
            
            else:
                high=mid-1
                # ans=min(ans,arr[mid])
                # index=low
                if(arr[mid]<ans):
                    ans=arr[mid]
                    index=mid

        return index
