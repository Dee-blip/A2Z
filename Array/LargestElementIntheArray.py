class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        if n==1:
            return arr[0]
        res=-1
        
        for i in arr:
            if res<i:
                res=i
        return res
