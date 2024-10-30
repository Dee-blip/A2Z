# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return root
        return self.isSymmetricHelper(root.left,root.right)


    def isSymmetricHelper(self,left,right):
        if left==None or right==None:
            return left==right #check the left or right node if both null it means its true then check both are null and it return True

        if left.val!=right.val:
            return False

        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
        
