# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeSort(self,l,r):
        dum=tail=ListNode(0)

        while l and r:
            if l.val<r.val:
                tail.next = l
                l=l.next
            else:
                tail.next = r
                r=r.next
            tail= tail.next
        if l:
            tail.next =l
            tail = tail.next
        if r:
            tail.next = r
            tail = tail.next
        return dum.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next ==None:
            return head
        # Will use Merge Sort
        # Divide the LL first
        s=head
        f=head
        temp=head
        
        while f and f.next is not None:
            temp=s
            s=s.next
            f=f.next.next

        temp.next = None
        l = self.sortList(head)
        r = self.sortList(s)

        return self.mergeSort(l,r)




        

        
