post=[]
inorder=[]
preorder=[]

stack=[[root],1]

if not root:
	return

while stack:
	temp = stack.pop()
	# PreOrder
	if temp[1]==1:
		preorder.append(temp[0].val)
		temp +=temp[1]
		stack.append(temp)
		if temp[0].left!=None:
			stack.append([temp[0].left,1])
	#Inorder
	elif temp[1]==2:
		inorder.append(temp[0].val)
		temp +=temp[1]
		stack.append(temp)
		if temp[0].right!=None:
			stack.append([temp[0].right,1])	

	#PostOrder		
	else:
		post.append(temp[0].val)

print(post)
print(inorder)
print(preorder)
