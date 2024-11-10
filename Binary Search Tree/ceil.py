
class Solution:
    def findCeil(self, root, inp):
        ceil = -1
        
        while root:
            if root.key == inp:
                return root.key
            
            if inp > root.key:
                # Move to the right subtree if the current node's value is less than the target value.
                #we don't update ceil here, because root.data can't be the ceiling. Moving to the right subtree
                #might bring us closer to inp without going below it.
                root = root.right
            else:
                # Update ceil and move to the left subtree.
                ceil = root.key #means there might be an even smaller value that is still greater than or equal to inp
                root = root.left
                
        return ceil
