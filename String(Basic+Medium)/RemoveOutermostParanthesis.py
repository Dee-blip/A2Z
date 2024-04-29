#https://leetcode.com/problems/remove-outermost-parentheses/description/
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        if s=="":
            return ""

        stack=[]
        c=0
        # We just adding the valid paranthesis in the stack , rest we are ignoring so when c!=0 and '(' then add in the stack c+=1 ,c!=1 then add ')' and count-=1 
        for i in s:
            if i=='(' and c==0:
                c+=1 
            elif i=='(' and c!=0:
                c+=1
                stack.append(i)
            elif i==')' and c!=1:
                stack.append(i)
                c-=1
            else:
                c-=1

        return "".join(stack)
        
            
                

            


            
            




        
