class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        if head == None:
            return None
    
        curr= head
        
        while curr!=None and curr.next!=None:
            if curr.data == curr.next.data:
                duplicate = curr.next
                curr.next = duplicate.next
                
                if duplicate.next:
                    duplicate.next.prev=curr
                    
            else:
                curr = curr.next
        return head
                
