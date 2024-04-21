#https://www.naukri.com/code360/problems/insert-node-at-the-beginning_8144739?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next




def insertAtFirst(list: Node, newValue: int) -> Node:
    newNode=Node(newValue)
    if list==None:
        list=newNode
    else:
        newNode.next=list
        list= newNode
        return list





