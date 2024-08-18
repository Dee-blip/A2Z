# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head

        length=0
        temp= head
        while temp is not None:
            temp=temp.next
            length+=1

        mid=length//2
        count=0
        temp1=head
        prev=None
        while temp1 is not None:
            if count==mid:
                if mid==0 and count==0:
                    head=head.next
                else:
                    prev.next=temp1.next
            count+=1
            prev=temp1
            temp1=temp1.next

        return head



        
