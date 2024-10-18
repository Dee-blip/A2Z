class Solution:
    #Function to delete all the occurances of a key from the linked list.
    def deleteAllOccurOfX(self, head, x):
        
        temp = head
        
        
        while temp:
            if temp.data == x:
                
                if temp.prev == None:
                    head = head.next
                    if head:
                        head.prev = None
                else:
                    temp.prev.next = temp.next
                    if temp.next:
                        temp.next.prev = temp.prev
                
                temp= temp.next
            else:
                temp = temp.next
        
        return head
