# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        #idea is simple here cal the length of both of the head then whose length is greater than accordingly push the head to the next pointer
        # optimized solu
        length1=0
        length2=0
        tempA1,tempB1= headA,headB
        while tempA1 :
            length1+=1
            tempA1=tempA1.next
        while tempB1:
            if tempB1:
                length2+=1
                tempB1=tempB1.next
        if length1 < length2:
            while length1<length2:
                headB = headB.next
                length2-=1
        else:
            while length1!=length2:
                headA = headA.next
                length1-=1

        tempA=headA
        tempB=headB

        while tempA!=tempB:
            tempA=tempA.next
            tempB=tempB.next
        return tempA
