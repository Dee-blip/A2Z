from collections import deque, OrderedDict

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        ans=[]
        if not root:
            return ans
            
        top_view= OrderedDict()
        q = deque([(root,0)])
        
        while q:
            node,hd = q.popleft()
            
            if hd not in top_view:
                top_view[hd] = node.data
                
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
                
                
                        
        for key in sorted(top_view.keys()):
            ans.append(top_view[key])
        
        return ans
