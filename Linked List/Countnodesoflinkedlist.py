'''
Following is the structure of the Node class already defined.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
'''

def length(head) :
    temp=head
    count=0
    while temp is not None:
        count+=1
        temp=temp.next

    return count
