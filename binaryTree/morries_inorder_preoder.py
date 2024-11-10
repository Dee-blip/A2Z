# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Morris Preorder Traversal
        result = []
        curr = root
        
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right

            else:
                left_child = curr.left

                while left_child.right and left_child.right!=curr:
                    left_child = left_child.right

                if not left_child.right:
                    left_child.right = curr
                    result.append(curr.val)
                    curr = curr.left

                else:
                    left_child.right = None # when this condition met then, left_child.right!=curr
                    curr = curr.right
        return result




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Morris Inorder Traversal
        result = []
        curr = root
        
        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right

            else:
                left_child = curr.left

                while left_child.right and left_child.right!=curr:
                    left_child = left_child.right

                if not left_child.right:
                    left_child.right = curr
                    curr = curr.left

                else:
                    left_child.right = None
                    result.append(curr.val)
                    curr = curr.right
        return result









        # ans=[]
        # stack=[]
        # curr=root
        # while curr or stack:
        #     while curr:
        #         stack.append(curr)
        #         curr=curr.left
        #     curr=stack.pop()
        #     ans.append(curr.val)

        #     curr=curr.right
        # return ans
                    

     
        
