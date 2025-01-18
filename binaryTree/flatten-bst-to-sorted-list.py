
class Solution:
    def flattenBST(self, root):
        newNode = Node(-2)
        self.prev = newNode
        
        self.inorder(root)
        #detach the dummy node and return the flattened node
        self.prev.left = None
        self.prev.right = None
        return newNode.right
        
        
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            
            self.prev.left = None
            self.prev.right = root
            self.prev = root
        
            self.inorder(root.right)
