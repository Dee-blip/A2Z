class Solution:
    def constructDLL(self, arr):
     
        if not arr:
            return None
        head = Node(arr[0])
            
        tail = head 
        for i in range(1,len(arr)):
            node = Node(arr[i])
            tail.next = node
            node.prev= tail
            tail = node
        return head
