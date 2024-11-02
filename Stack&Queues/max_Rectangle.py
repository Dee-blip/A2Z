class Solution:
    def maxHisto(self,heights):
        n= len(heights)

        pse=[-1]*n
        nse=[n]*n

        #Previous Smaller Element
        stack=[]
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if not stack:
                pse[i] = -1
            else:
                pse[i] = stack[-1]
            stack.append(i)

        stack.clear()

        #Next Smaller Element
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)

        max_area=0

        for i in range(n):
            max_area=max(max_area,(nse[i]-pse[i]-1)*heights[i])
        return max_area


    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [[int(element) for element in row] for row in matrix]
        #consider only 1 that contain the building
        currMat = matrix[0]
        maxArea = self.maxHisto(currMat)

        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    currMat[j]+=1
                else:
                    currMat[j] = 0

            currAns = self.maxHisto(currMat)

            maxArea = max(maxArea, currAns)

        return maxArea
