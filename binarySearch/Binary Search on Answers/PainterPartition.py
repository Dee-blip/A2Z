def checkLengthisEqual(nums,check):
    painter =1
    lengthIncrement = 0

    for i in range(len(nums)):
        if lengthIncrement + nums[i] <=check:
            lengthIncrement+=nums[i]
        else:
            painter +=1
            lengthIncrement=nums[i]
    return painter

def splitArray(nums: list, k: int) -> int:
    if k>len(nums):
        return -1

    low = max(nums)
    high = sum(nums)
    ans = float('inf')

    while low<=high:
        mid=(low+high)//2

        if checkLengthisEqual(nums,mid)<=k:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

def findLargestMinDistance(boards:list, k:int):
    return splitArray(boards,k)



        
