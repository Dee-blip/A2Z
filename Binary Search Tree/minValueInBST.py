
class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        if root==None:
            return -1
       
        if not root.left and not root.right:
            return root.data
        
        if root.left is None:
            return root.data
        
        return self.minValue(root.left)
