

class Solution:
    def evenlyDivides (self, N):
        temp= N
        count=0
        while N!=0:
            divisor = N%10
            if  divisor!=0  and temp%divisor==0 :
                count+=1
            N//=10
        return count
            
            
        # code here

