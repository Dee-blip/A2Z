# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = deque([(root,0)])
        while queue:
            length = len(queue)

            first_node , first_index = queue[0]

            for i in range(length):
                node,index = queue.popleft()
                if node.left:
                    queue.append((node.left,2*(index-first_index)+1))
                if node.right:
                    queue.append((node.right,2*(index-first_index)+2))
                last_index= index

            max_width = max(max_width, last_index - first_index+1)

        return max_width
