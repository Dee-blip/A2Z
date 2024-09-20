class MyStack:


    # class StackNode:

    # # Constructor to initialize a node
    # def __init__(self, data):
    #     self.data = data
    #     self.next = None
    def __init__(self):
        self.head=None
        self.count=0
        
    #Function to push an integer into the stack.
    def push(self, data):
        newnode= StackNode(data)
        newnode.next=self.head
        self.head= newnode
        self.count+=1
        return self.head
    
    #Function to remove an item from top of the stack.
    def pop(self):
        if self.count==0:
            return -1
        popped_node= self.head.data
        self.head= self.head.next
        return popped_node

        # Add code here
