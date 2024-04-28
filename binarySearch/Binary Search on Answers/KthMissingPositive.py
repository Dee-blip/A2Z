https://leetcode.com/problems/kth-missing-positive-number/description/
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Brute Force Approach
        # for i in range(len(arr)):
        #     if arr[i]<=k:
        #         k+=1
        #     else:
        #         break
        # return k

        #binary Search
        low=0
        high=len(arr)-1

        while low<=high:
            mid=(low+high)//2

            missing=arr[mid]-(mid+1)

            if missing <k:
                low=mid+1
            else:
                high=mid-1
        return low+k
            
