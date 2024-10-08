https://leetcode.com/problems/asteroid-collision/description/
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        n=len(asteroids)

        for i in range(n):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and abs(asteroids[i]) > stack[-1]:
                    stack.pop()
                if stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif not stack or (stack[-1]<0 and asteroids[i]<0):
                    stack.append(asteroids[i])
        return stack
