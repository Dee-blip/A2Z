'''

class Solution:
    #Function to check whether all nodes of a tree have the value 
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):
        if root is None:
            return 1
            
  
        if  not root.left and not root.right:
            return 1
            
        left = root.left.data if root.left else 0
        right = root.right.data if root.right else 0
        
        
        if root.data != left + right:
            return 0
        return self.isSumProperty(root.left) and self.isSumProperty(root.right)
