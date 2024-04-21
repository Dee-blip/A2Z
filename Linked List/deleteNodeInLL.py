#https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # think about coping the variable of next LL value and then linked the current node to next-next node 
        node.val= node.next.val
        node.next=node.next.next

