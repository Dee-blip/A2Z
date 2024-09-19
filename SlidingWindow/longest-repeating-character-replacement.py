class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        n=len(s)

        ans=0
        maxf=0
        d={}
        while j<n:
            d[s[j]]=d.get(s[j],0)+1
            maxf = max(maxf,d[s[j]])

            while (j-i+1)- maxf >k:
                d[s[i]]-=1
                i+=1
            ans= max(ans,j-i+1)
            j+=1
        return ans
        
