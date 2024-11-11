# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #for kth Largest just reversal inorder morris traversal just change all the left to right,right to left
    #traverse first right subtree and then left subtree
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        curr = root

        while curr:
            if curr.left is None:
                count+=1
                if count==k:
                    return curr.val
                curr = curr.right

            else:
                left_child = curr.left

                while left_child.right and left_child.right!=curr:
                    left_child = left_child.right

                if left_child.right is None:
                    left_child.right = curr
                    curr = curr.left
                else:
                    left_child.right = None
                    count+=1
                    if count==k:
                        return curr.val
                    curr = curr.right
                   

        
