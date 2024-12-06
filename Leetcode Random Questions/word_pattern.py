class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(words)!=len(pattern):
            return False

        dic = {}
        used_chars = set()
        
        for i in range(len(pattern)):
            word = words[i]
            char = pattern[i]

            if word not in dic:
                if char in used_chars:
                    return False
                dic[word] = char
                used_chars.add(char)
            elif dic[word] != char:
                    return False

        return True
