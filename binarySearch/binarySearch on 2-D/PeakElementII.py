#https://leetcode.com/problems/find-a-peak-element-ii/description/
from typing import List

class Solution:

    def getPeak(self, matrix, col: int) -> int:
        maxV = -1
        index = -1

        for i in range(len(matrix)):
            if matrix[i][col] > maxV:
                maxV = matrix[i][col]
                index = i
        return index

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        low = 0
        high = m - 1

        while low <= high:
            mid = (low + high) // 2
            ans = self.getPeak(mat, mid)

            left = mat[ans][mid - 1] if mid - 1 >= 0 else -1
            right = mat[ans][mid + 1] if mid + 1 < m else -1

            if mat[ans][mid] > left and mat[ans][mid] > right:
                return [ans, mid]
            elif mat[ans][mid] < left:
                high = mid - 1
            else:
                low = mid + 1

        return [-1, -1]
