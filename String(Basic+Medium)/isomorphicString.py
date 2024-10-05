class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        d1={}
        d2={}

        for i in range(len(s)):
            if (d1.get(s[i])!=None and d1.get(s[i])!=t[i]) or (d2.get(t[i])!=None and d2.get(t[i])!=s[i]):
                return False

            d1[s[i]]=t[i]
            d2[t[i]]=s[i]
        return True
