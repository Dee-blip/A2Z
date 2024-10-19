"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        # Create new noded interleaved with the original nodes
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # set the random pointer for the copied nodes
        curr= head

        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr=curr.next.next
        
        #separation process
        curr = head
        copied = head.next
        temp = copied

        while curr is not None:
            curr.next  = curr.next.next
            if copied.next:
                copied.next= copied.next.next
            curr = curr.next
            copied = copied.next
        return temp



        
        
