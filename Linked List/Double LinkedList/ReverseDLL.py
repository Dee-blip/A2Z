class Solution:
    def reverseDLL(self, head):
        if not head:
            return None
            
        
        temp = head
        prev = None
        
        while temp is not None:
            temp.prev,temp.next = temp.next, temp.prev
            prev = temp
            temp = temp.prev
            
        return prev
