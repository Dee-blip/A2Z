class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        total_beauty = 0
        
        for i in range(n):
            freq = {}
    
            for j in range(i, n):
                freq[s[j]] = freq.get(s[j],0)+1
                max_freq = max(freq.values())
                min_freq = min(freq.values())
                
                total_beauty += max_freq - min_freq
        
        return total_beauty
