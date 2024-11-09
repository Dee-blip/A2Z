# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        res = []

        while queue:
            node = queue.popleft()
            if not node:
                res.append("null")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
       
        return ','.join(res)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return []

        vals = deque(data.split(","))
        root = TreeNode(vals.popleft())
        q = deque([root])

        while q and vals:
            node = q.popleft()
            left = vals.popleft()
            right = vals.popleft()

            if left!="null":
                node.left = TreeNode(int(left))
                q.append(node.left)
            if right!="null":
                node.right = TreeNode(int(right))
                q.append(node.right)

        return root
                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
