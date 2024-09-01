class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        maxCount=0
        res=""
        d={}

        while j<n:
            res+=s[j]
            if s[j] in d:
                d[s[j]]+=1
            else:
                d[s[j]]=1
            
            if len(d)==j-i+1:
                maxCount=max(maxCount,len(res))

            elif j-i+1>len(d):
                while j-i+1>len(d):
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        d.pop(s[i])
                    res=res[1:]
                    i+=1
            
            j+=1
        return maxCount


        
