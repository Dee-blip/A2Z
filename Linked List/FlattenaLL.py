class Solution:
    def flatten(self,root):
        if root==None or root.next==None:
            return root
            
        root.next=self.flatten(root.next)
        root=self.merge(root,root.next)
        
        return root
    
    def merge(self,a,b):
        temp=Node(0)
        result=temp
        
        while a!=None and b!=None:
            if a.data<b.data:
                # lookse the meaning of original botton pointers and mix the top level list strucutre
                temp.bottom=a
                temp=temp.bottom
                a=a.bottom
            else:
                temp.bottom=b
                temp=temp.bottom
                b=b.bottom
        if a:
            temp.bottom=a
        else:
            temp.bottom=b
        return result.bottom
