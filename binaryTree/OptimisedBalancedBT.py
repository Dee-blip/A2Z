# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkTree(self,root):
        if root==None:
            return 0
        
        left = self.checkTree(root.left)
        right = self.checkTree(root.right)

        if left ==-1:
            return -1
        if right == -1:
            return -1
        # print(left)
        # print(right)
        # print(abs(left - right))
        if abs(left - right)>1:
            return -1
    
        return 1+ max(left,right)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        return self.checkTree(root) != -1
        


        
