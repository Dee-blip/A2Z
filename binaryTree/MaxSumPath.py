# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMaxiSum(self,root,arr):
        if root==None:
            return 0
        left=max(0,self.getMaxiSum(root.left,arr)) #never take negative left sum path
        right=max(0,self.getMaxiSum(root.right,arr))#never take negative right sum path

        arr[0]=max(arr[0],left+right+root.val)

        return root.val + max(left,right)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        arr = [float('-inf')]
        self.getMaxiSum(root,arr)

        return arr[0]
        
