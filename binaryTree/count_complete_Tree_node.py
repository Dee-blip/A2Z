class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        left_height = self.findHeightLeft(root)
        right_height = self.findHeightRight(root)

        if left_height == right_height:
            return (2 ** left_height) - 1
        else:
            #  1 is for the current node
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def findHeightLeft(self, node: TreeNode) -> int:
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def findHeightRight(self, node: TreeNode) -> int:
        height = 0
        while node:
            height += 1
            node = node.right
        return height
