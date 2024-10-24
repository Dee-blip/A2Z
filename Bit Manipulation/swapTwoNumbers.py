class Solution:
    def get(self, a, b):
        res=[]
        
        a = a ^ b
        b = a ^ b
        a = a ^ b
        res.append(a)
        res.append(b)
        
        return res
