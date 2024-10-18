class Solution:
    def delete_node(self, head, x):
        if head == None:
            return None
        temp= head
        count=1
        while temp:
            if count == x:
                break
            count+=1
            temp=temp.next
        

        if temp is None:
            return head
            
        if temp.prev is None:
            head =temp.next
            if head:
                head.prev = None
        
        elif temp.next==None:
            store = temp.prev
            store.next =None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        
        return head
