class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    
    
    def minRightSubtree(self,root):
        curr = node
        while curr.left:
            curr = curr.left
        return curr
    def inorderSuccessor(self, root, x):
        successor = None
        
        if x.right is not None:
            return self.minRightSubtree(x.right)
        
        while root:
            if x.key < root.key:
                successor = root
                root = root.left
            elif x.key>root.key:
                root = root.right
            else:
                break
        return successor
        
