# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Time Complexity is O(n*n)
    # def getBSTLength(self,root):
    #     if root==None:
    #         return 0
    #     return 1+max(self.getBSTLength(root.left),self.getBSTLength(root.right))
    
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if root==None:
    #         return True
            
    #     left=self.getBSTLength(root.left)
    #     right=self.getBSTLength(root.right)

    #     if left - right>1 or right-left>1:
    #         return False
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

