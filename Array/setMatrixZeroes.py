class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        seti=set()
        setj=set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    seti.add(i)
                    setj.add(j)


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in seti or j in setj:
                    matrix[i][j]=0
        return matrix


        
