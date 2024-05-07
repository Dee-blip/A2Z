#https://leetcode.com/problems/search-a-2d-matrix/
class Solution:

    def binarySearch(self,searchMat,target):
        low=0
        high=len(searchMat)-1
        while low<=high:
            mid=(low+high)//2
            if searchMat[mid]==target:
                return True
            elif searchMat[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for i in range(len(matrix)):
            boolAns= self.binarySearch(matrix[i],target)
            if boolAns==True:
                return True
        return False
        
    

        
