# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head

        o=head
        e=dum=head.next
        while e and e.next:
            o.next=o.next.next
            # print(o.next.val)
            e.next=e.next.next
            
            o=o.next
            print(o.val)
            e=e.next
            # print(e.val)
        o.next=dum

        return head

















        
