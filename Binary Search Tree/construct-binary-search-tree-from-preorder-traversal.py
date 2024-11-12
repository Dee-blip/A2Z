# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(lower,upper):
            nonlocal idx
            if idx == len(preorder) or preorder[idx] < lower or preorder[idx] > upper:
                return None
            val = preorder[idx]

            idx+=1

            root = TreeNode(val)

            root.left = helper(lower,val)
            root.right = helper(val,upper)

            return root

        idx=0
        return helper(float('-inf'),float('inf'))
