
class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        newNode = Node(x)
        if head==None:
            return newNode
        
        temp=head
        count=0
        
        while temp is not None:
            if count==p:
                break
            count+=1
            temp=temp.next
            
        newNode = Node(x)
        if temp.next==None:
            temp.next = newNode 
        else:
            store=temp.next
            temp.next = newNode 
            newNode.next= store
            store.prev= newNode
        newNode.prev = temp
        
        return head
