'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def traverseBoundary(root):
    if not root:
        return []

    boundary = []
    boundary.append(root.data)


    def left_node_excluding_leafNode(node):
        if node:
            if node.left or node.right:
                boundary.append(node.data)
            if node.left:
                left_node_excluding_leafNode(node.left)
            else:
                left_node_excluding_leafNode(node.right)

    def leafNode(node):
        if node:
            if not node.left and not node.right:
                boundary.append(node.data)
            leafNode(node.left)
            leafNode(node.right)
    

    def right_node_excluding_leafNode(node):
        if node:
            if node.right or node.left:
                if node.right:
                    right_node_excluding_leafNode(node.right)
                else:
                    right_node_excluding_leafNode(node.left)
                boundary.append(node.data)


    left_node_excluding_leafNode(root.left)
    leafNode(root)
    right_node_excluding_leafNode(root.right)

    return boundary
    
