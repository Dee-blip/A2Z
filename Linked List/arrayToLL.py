class Solution:
    def constructLL(self, arr):
        head=Node(arr[0])
        temp = head
        
        for i in range(1,len(arr)):
            nodeCreation= Node(arr[i])
            temp.next= nodeCreation
            temp=nodeCreation
            
            
       
        return head
            
