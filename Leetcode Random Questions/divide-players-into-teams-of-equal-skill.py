class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        i=1
        j=n-2
        target = skill[0] + skill[-1]
        ans=skill[0]*skill[-1]
        while i<j:
            if skill[i]+skill[j]==target:
                ans+=(skill[i] * skill[j])
                i+=1
                j-=1
            else:
                return -1
        return ans



        
