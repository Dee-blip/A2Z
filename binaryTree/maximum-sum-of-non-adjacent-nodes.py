class Solution:
    def getMaxSum(self,root):
    
        memo = {}
        
        if not root:
            return 0
        
        def helper(node):
            if not node:
                return (0,0)
            if node in memo:
                return memo[node]
                
            left_include, left_exclude = helper(node.left)
            right_include, right_exclude = helper(node.right)
            
            include = node.data + left_exclude + right_exclude
            exclude = max(left_include, left_exclude) + max(right_include, right_exclude)
            
            memo[node] = (include,exclude)
            
            return (include,exclude)
            
        
        include , exclude = helper(root)
        return max(include,exclude)
