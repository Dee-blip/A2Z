#https://www.naukri.com/code360/problems/allocate-books_1090540?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=PROBLEM
def checkStudentsGettingBooks(arr, pages):
    student = 1
    noOfPages = 0
    for i in range(len(arr)):
        if noOfPages + arr[i] <= pages:
            noOfPages += arr[i]
        else:
            student += 1
            noOfPages = arr[i]

    return student



def findPages(arr: [int], n: int, m: int) -> int:
    if m>n:
        return -1

    low=max(arr)
    high=sum(arr)
    ans=float('inf')
    while low<=high:
        mid = (low+high)//2

        if checkStudentsGettingBooks(arr,mid)<=m:
            ans=mid
            high=mid-1

        else:
            low=mid+1

    return ans
    




            







