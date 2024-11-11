# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newNode = TreeNode(val)
        if root == None:
            return newNode

        curr = root

        while True:
            if curr.val<=val:
                if curr.right!=None:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break
            else:
                if curr.left!=None:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break

        return root
                
        
