class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.
#https://www.naukri.com/code360/problems/find-length-of-loop_8160455?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM


def lengthOfLoop(head: Node) -> int:
    if not head or not head.next:
        return 0

    s=head
    f=head
    while f and f.next is not None:
        s=s.next
        f=f.next.next

        if s==f:
            break
    if not f or not f.next:
        return 0
    s=head
    while s!=f:
        s=s.next
        f=f.next

    temp=s.next

    count=1

    while s!=temp:
        temp=temp.next
        count+=1
    return count


    
    
