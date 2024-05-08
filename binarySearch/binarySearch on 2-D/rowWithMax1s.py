"""
    Time Complexity: O(N * M)
    Space Complexity: O(1)

    Where N is the number of rows and M is the number of columns in the given matrix.
"""
#https://www.naukri.com/code360/problems/row-of-a-matrix-with-maximum-ones_982768?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
def lowerbound(check,key):
    low=0
    high=len(check)-1
    ans=999999
    while low<=high:
        mid=(low+high)//2

        if check[mid]>=key:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    if ans==9999:
        return -1
    return ans

    

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:
    index=-1
    current1Count=0

    for i in range(len(matrix)):
        ans=lowerbound(matrix[i],1)
        temp=len(matrix[i])-ans

        if temp> current1Count:
            current1Count=temp
            index=i
        
    return index
            
    



