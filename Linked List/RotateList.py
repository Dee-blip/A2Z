# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head

        length=0
        temp = head
        while temp:
            temp = temp.next
            length+=1

        k=k%length
        if k==0:
            return head
        
        while k>0:
            temp = head
            prev = None
            
            while temp.next is not None:
                prev= temp
                temp=temp.next
            # print(prev.val)
            prev.next = None
            temp.next = head
            head = temp
            k-=1
        return head

        
