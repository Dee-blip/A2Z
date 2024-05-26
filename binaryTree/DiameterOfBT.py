# Definition for a binary tree node. - O(n)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def height(self,root,arr):
        if root==None:
            return 0 
        left=self.height(root.left,arr)
        right=self.height(root.right,arr)
        arr[0]=max(arr[0],left+right)
        return 1+ max(left,right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #Longest path b/w 2 nodes
        # Path does not need to pass via root
        arr=[0]
        self.height(root,arr)
        return arr[0]


        
