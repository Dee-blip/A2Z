class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d={'a':0,'b':0,'c':0}
        count=0
        i=0
        j=0
        n=len(s)   
        while j<n:
            d[s[j]]+=1
            while d['a'] and d['b'] and d['c']:
                count+=n-j
                print(count)
                d[s[i]]-=1
                i+=1  
            j+=1
        return count
            

        
