class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):
        temp = head
        prev = None
        while temp is not None:
            store = temp.next
            temp.next = prev
            prev = temp
            temp = store
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 1:
            return head

        curr = head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        noOfRotationGroup = count // k
        prev_gp_end = None
        dummy = ListNode(0)
        dummy.next = head
        prev_gp_end = dummy

        while noOfRotationGroup > 0:
            gpprev = prev_gp_end.next
            gpcurr = gpprev

            tempK = k - 1
            while tempK > 0:
                gpcurr = gpcurr.next
                tempK -= 1
            
            next_gp_start = gpcurr.next
            gpcurr.next = None

            reversed_gp_head = self.reverse(gpprev)

            prev_gp_end.next = reversed_gp_head
            gpprev.next = next_gp_start
            prev_gp_end = gpprev

            noOfRotationGroup -= 1
            
        return dummy.next
