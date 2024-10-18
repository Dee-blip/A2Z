class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        count0=0
        count1=0
        count2=0
        temp=head
        while temp:
            if temp.data==0:
                count0+=1
            if temp.data==1:
                count1+=1
            if temp.data==2:
                count2+=1
                
            temp=temp.next
            
        dum=tail=Node(0)
        while count0>0:
            tail.next=Node(0)
            count0-=1
            tail=tail.next
        while count1>0:
            tail.next=Node(1)
            count1-=1
            tail=tail.next
        while count2>0:
            tail.next=Node(2)
            count2-=1
            tail=tail.next
            
        return dum.next
