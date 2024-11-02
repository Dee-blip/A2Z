class Solution:
    def makeFancyString(self, s: str) -> str:

        stack = []
        count = 0
        prev = ''

        for char in s:
            if char == prev:
                count += 1
            else:
                count = 1
            if count<3:
                stack.append(char)
            prev = char

        return "".join(stack)
                 
