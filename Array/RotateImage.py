class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                # print(i,j)
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
        for i in range(len(matrix)):
            matrix[i]=reversed(matrix[i])
        return matrix


        
