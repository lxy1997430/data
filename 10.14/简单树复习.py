from pprint import pformat
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(Node.data)
        return pformat({"%s"%(self.data):(self.left,self.right)})


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def add(self,item):
        node = Node(item)

        if self.root is None:
            self.root = node
        else:
            temp = [self.root]

            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return #为什么不yongbreak
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def getParent(self,node):
