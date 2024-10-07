class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        if not s:
            return
        top_element = s.pop()
        self.Sorted(s)
        self.insert_element(s,top_element)
        
        
        
    def insert_element(self,stack,element):
        if not stack or element>stack[-1]:
            stack.append(element)
        else:
            temp=stack.pop()
            self.insert_element(stack,element)
            stack.append(temp)
