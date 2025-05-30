# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #First approach is to use level order traversal and take out the last element of the each array but space complexity will be big
        #use recursive solution 
        #. 1- Cleaner and Readable code , 2- we can pass local variable and parameter to the dfs function 
        right=[]
        def dfs(root,level):
            if root==None:
                return []
            if level == len(right):
                right.append(root.val)

            dfs(root.right,level+1)
            dfs(root.left,level+1)

        dfs(root,0)

        return right
       
