from collections import deque, OrderedDict

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def bottomView(self,root):
        ans=[]
        if not root:
            return ans
            
        bottom_view= OrderedDict()
        q = deque([(root,0)])
        
        while q:
            node,hd = q.popleft()
            
            
            bottom_view[hd] = node.data
                
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
                
                
                        
        for key in sorted(bottom_view.keys()):
            ans.append(bottom_view[key])
        
        return ans
