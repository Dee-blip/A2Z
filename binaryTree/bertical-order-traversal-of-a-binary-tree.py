from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        column_table = defaultdict(list)
        nodes = [(0, 0, root)] 
        index = 0  

        while index < len(nodes):
            hd, depth, node = nodes[index]
            index += 1

            column_table[hd].append((depth, node.val))

            if node.left:
                nodes.append((hd - 1, depth + 1, node.left))
            if node.right:
                nodes.append((hd + 1, depth + 1, node.right))

        ans = []
        for i in sorted(column_table.keys()):
            ans.append(sorted(column_table[i]))
        # print(ans)
        result = []
        for column in ans:
            flatten=[]
            for depth,val in column:
                flatten.append(val)
            result.append(flatten)
        return result
