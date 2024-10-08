class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            curr=[]
            for j in range(i+1):
                if j==0 or i==j:
                    curr.append(1)
                else:
                    curr.append(res[i-1][j-1]+res[i-1][j])
            res.append(curr)
            
        return res
