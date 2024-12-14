class Solution:
    def search(self, pat, txt):
        def build_lps(pattern):
            m = len(pattern)
            lps = [0] * m 
            
            length = 0
            
            i = 1
            
            while i<m:
                if pattern[length] == pattern[i]:
                    length+=1
                    lps[i] = length
                    i+=1
                else:
                    if length !=0:
                        length = lps[length-1]
                    else: #to cover out of bound issue here
                        lps[i] = 0
                        i+=1
            return lps
            
        lps = build_lps(pat)
        
        result = []

        i=0
        j=0
        
        n = len(txt)
        while i<n:
            
            if txt[i] == pat[j]:
                i+=1
                j+=1
            if j == len(pat):
                result.append(i-j)
                j = lps[j-1]
                
            elif i<len(txt) and txt[i]!=pat[j]:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return result
