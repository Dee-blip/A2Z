# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow,fast = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head1 = head
        head2 = slow.next
        slow.next = None

        head2 = self.reverse(head2)


        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next

            head1.next = head2
            if temp1 is None:
                break
            head2.next = temp1
            head1 = temp1
            head2 = temp2
            





        
        
