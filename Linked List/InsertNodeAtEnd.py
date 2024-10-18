class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        if head==None:
            return Node(x)
        
        tail = head
        prev=None
        while tail is not None:
            prev = tail
            tail=tail.next
            
        prev.next = Node(x)
        
        return head
