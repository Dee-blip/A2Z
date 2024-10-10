# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None :
            return True
        s=head
        f=head
        while f and f.next is not None:
            s=s.next
            f=f.next.next
       
        prev=None
        
        while s is not None:
            s.next,s,prev = prev,s.next,s
        
            
            
        first=head
        sec=prev
        while first and sec:
            if first.val!=sec.val:
                return False

            first=first.next
            sec=sec.next
        return True
