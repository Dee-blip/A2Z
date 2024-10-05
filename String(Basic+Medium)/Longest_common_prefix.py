class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
       
        min1=min(len(i) for i in strs)
        check = list(strs[0])[:min1]
        j=0
        ans=""
        while j<min1:
            for i in range(1,len(strs)):
                if strs[i][j]!=check[j]:
                    return ans
            ans+=check[j]
            j+=1
        return ans

        

            
