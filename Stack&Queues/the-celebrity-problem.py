class Solution:
    def celebrity(self, mat):
        n=len(mat)
        top=0
        down= len(mat)-1
        
        while top<down:
            if mat[top][down]==1:
                top+=1
            elif mat[down][top]==1:
                down-=1
        
            else:
                top+=1
                down-=1

        for i in range(n):
            if i!=top:
                if(mat[top][i]==1 or mat[i][top]==0):
                    return -1
                
        return top
