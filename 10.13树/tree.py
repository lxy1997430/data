#先进先出,用数组也可以,用队列也可以.用队列需要导包
#用数组接收经历的根节点
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class Tree:
    def __init__(self):
        self.root = None

    def add(self,item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]#用一个数组存储遍历过的根节点
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def getPrent(self,item):
        if self.root == item:
            return None
        else:

            res = [self.root]
            while res:
                pop_node = res.pop(0)
                if pop_node.left.data == item:
                    return pop_node

                if pop_node.right.data == item:
                    return pop_node
                if pop_node.left:
                    res.append(pop_node.left)
                if pop_node.right:
                    res.append(pop_node.right)
            return None

if __name__ == '__main__':
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    t.add(5)
    print(t.root.left.left)

