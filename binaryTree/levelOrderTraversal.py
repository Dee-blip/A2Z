# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        queue=[]
        if root==None:
            return ans
        queue.append(root)
        while len(queue):
            size=len(queue)  
            level=[]
            for i in range(size):
                node=queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                
            ans.append(level)
        return ans
                


        
