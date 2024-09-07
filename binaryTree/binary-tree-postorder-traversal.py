# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #using one stack
        curr=root
        stack=[]
        res=[]
        while curr is not None or len(stack)!=0 :
            if curr!=None:
                stack.append(curr)
                curr=curr.left
            else:
                temp = stack[-1].right
                if(temp==None):
                    temp=stack[-1]
                    stack.pop()
                    res.append(temp.val)
                    while len(stack)!=0 and temp==stack[-1].right:
                        temp=stack[-1]
                        stack.pop()
                        res.append(temp.val)
                else:
                    curr=temp
        return res

        # using 2 stack
        # if root==None:
        #     return []

        # stack1=[]
        # stack2=[]

        # res=[]
        # #post order-  Left Right Root
        # stack1.append(root)
        # while(len(stack1)!=0):
        #     temp= stack1[-1]
        #     stack1.pop()
        #     stack2.append(temp)

        #     if temp.left is not None:
        #         stack1.append(temp.left)
        #     if temp.right is not None:
        #         stack1.append(temp.right)
    
        # for i in range(len(stack2)-1,-1,-1):
        #     res.append(stack2[i].val)

        # return res


