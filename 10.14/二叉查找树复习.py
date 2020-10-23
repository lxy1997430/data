#存放数据或者用来查找数据
from pprint import pformat
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(Node.data)
        return pformat({"%s"%(self.data):(self.left,self.right)})


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)



    def search(self,value):
        if self.root is None:
            raise IndexError("search from empty tree")
        else:

            temp = self.root
            while temp and value != temp.data:
                if value < tepm.data:
                    temp = temp.left
                elif value > temp.data:
                    temp = temp.right
            return temp

    def is_right(self,node):
        return node == node.parent.right
#二叉树中没有相同的数值
#子节点指不指向父节点我不管,只要父节点没有指向他就算没有了(不在树上)
    def  _reassign_node(self,node,new_children):
        if new_children is not None:#找父亲,如果为空就不用找,空节点没有这个属性
            new_children.parent = node.parent
        if node.parent is not None:#找孩子
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:#根节点没有父亲
            self.root = new_children

    def remove(self,value):
        if self.root is None:
            raise IndexError("remove from empty tree")
        else:
            node = self.search(value)
            if node.left is None and node.right is None:#没有孩子节点
                self._reassign_node(node,None)
            elif node.right is None:#只有左孩子
                self._reassign_node(node,node.left)
            elif node.left is None:#只有右孩子
                self._reassign_node(node,node.right)
                #既有左孩子又有右孩子
            else:#为了避免替换下面一大长串,可以用一种偷梁换柱的想法,只要值在就行
                temp = self.getMax(node.left)#找到左子树的最大节点(传入一个根节点)
                self.remove(temp.value)
                node.value = temp.value

    def getMax(self):
        pass

