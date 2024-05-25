# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        return [root.val] +self.preorderTraversal(root.left) +self.preorderTraversal(root.right) 
        

# Iterative
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None or root==[]:
            return []
        ans=[]
        q=[root]  
        while len(q):
            temp=q.pop()
            ans.append(temp.val)
             
            if temp.right is not None:
                q.append(temp.right)
            if temp.left is not None:
                q.append(temp.left)

        return ans

             
