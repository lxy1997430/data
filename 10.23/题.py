#判断两棵二叉树是否相同
#递归
def isSame(node1,node2):
    if node1 is None and node2 is None:
        return True
    # elif node1:
    #     return False
    # elif node2:
    #     return False
    if node1 is None or node2 is None:
        return False
    if node1.value != node2.value:
        return False
    return isSame(node1.left,node2.left) and isSame(node1.right,node2.right)


#栈






