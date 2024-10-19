class Solution:
    
    def reverseList(self,head):
        prev=None
        current =head
        
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    def addOne(self,head):
        head = self.reverseList(head)
        
        curr = head
        carry = 1
        
        while curr is not None:
            curr.data+=carry
            
            if curr.data>=10:
                curr.data -= 10
                carry=1
            else:
                carry = 0 
        
            if curr.next is None and carry:
                new_node = Node(carry)
                curr.next = new_node
                carry = 0
                
            curr=curr.next
            
        head = self.reverseList(head)
        
        return head
