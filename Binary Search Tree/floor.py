class Solution:
    def floor(self, root, x):
        floor = -1
        
        while root:
            if root.data == x:
                return root.data
            
            if x > root.data:
                floor = root.data
                root = root.right
            else:
                root = root.left
                
        return floor
