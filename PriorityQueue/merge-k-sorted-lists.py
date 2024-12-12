# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #getting all the elements from the linked lists, sorting them, and then transforming them back into a linked list. - O(NLog N)
        # we can use priority queue min-heap as it mentioned linkedList should be ascending order
        
        min_heap=[]
        # Step 1: Add the first node of each list into the heap
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap,(node.val,i,node))

        D = ListNode()
        curr = D

        # Step 3: Extract the smallest element from the heap and add to the merged list
        while min_heap:
            val,i,node = heapq.heappop(min_heap)

            curr.next = node
            curr = node
            node = node.next

            if node:
                heapq.heappush(min_heap,(node.val,i,node))

        return D.next
