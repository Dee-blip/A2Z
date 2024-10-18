# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None:
            return []

        temp=head
        length=0

        while temp is not None:
            temp=temp.next
            length+=1

        target=length- n
        count=0
        temp2=head
        prev=None

        while count<target :
            prev=temp2
            temp2=temp2.next
            count+=1
        
        if prev is not None:
            prev.next=temp2.next
        else:
            head=head.next
        return head
