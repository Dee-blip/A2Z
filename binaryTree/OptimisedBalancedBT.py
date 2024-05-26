# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity is O(n*n)
    def checkHeight(self,root):
        if root==None:
            return 0
        left=self.checkHeight(root.left)
        if left==-1:
            return -1
        right=self.checkHeight(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1   
        return 1+max(self.checkHeight(root.left),self.checkHeight(root.right
        ))     
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.checkHeight(root)!= -1

