#遇到递归,树(传统节点树,字典树)时可以画线程栈
from pprint import pformat
class Node:
    def __init__(self,value,parent):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s"%(self.value):(self.left,self.right)},indent=1)#indent缩进


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
        # return True if self.root is None else False
    def __insert(self,value):
        node = Node(value,parent=None)
        if self.is_empty():
            self.root = node
        else:
            parent_node = self.root
            while True:

                if value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = node
                        break
                    else:
                        parent_node = parent_node.right

            node.parent = parent_node#还要给他制定父母

    def insert(self,*values):#不定长参数,元组?
        for value in values:
            self.__insert(value)
        return self

    def search(self,value):
        if self.is_empty():
            raise IndexError("search from empty tree")
        else:
            node = self.root
            while node and node.value != value:
                if value < node.value:
                    node = node.left
                elif value > node.value:
                    node = node.right#有时候条件可以放在while后面,不满足条件循环结束时输出结果
            return node

        # 二叉树中没有相同的数值
        # 子节点指不指向父节点我不管,只要父节点没有指向他就算没有了(不在树上)
    def _reassign_node(self, node, new_children):
        if new_children is not None:  # 找父亲,如果为空就不用找,空节点没有这个属性
            new_children.parent = node.parent
        if node.parent is not None:  # 找孩子
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:  # 根节点没有父亲
            self.root = new_children

    def remove(self, value):
        if self.root is None:
            raise IndexError("remove from empty tree")
        else:
            node = self.search(value)
            if node.left is None and node.right is None:  # 没有孩子节点
                self._reassign_node(node, None)
            elif node.right is None:  # 只有左孩子
                self._reassign_node(node, node.left)
            elif node.left is None:  # 只有右孩子
                self._reassign_node(node, node.right)
                # 既有左孩子又有右孩子
            else:  # 为了避免替换下面一大长串,可以用一种偷梁换柱的想法
                temp = self.getMax(node.left)  # 找到左子树的最大节点(传入一个根节点)
                self.remove(temp.value)
                node.value = temp.value

    def getMax(self,node):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right:
                node = node.right
        return node

    def getMin(self,node):
        if node is None:
            node = self.root
        if not self.is_empty():
            # node = self.root
            while node.left:
                node = node.left
        return node

    #前序遍历
    #利用递归实现(递归的执行顺序跟树相似),放到线程栈中,调试模式可见
    def preOrderTraverse1(self,node):
        if not node:#为空时退出(出口)
            return None
        print(node.value)
        self.preOrderTraverse1(node.left)#压栈的方式是调用函数,弹栈的方式是return
        self.preOrderTraverse1(node.right)#每一次都是单独的一次调用函数

    def zhongxu(self,node):
        if not node:#为空时退出(出口)
            return None

        self.preOrderTraverse1(node.left)#压栈的方式是调用函数,弹栈的方式是return
        print(node.value)
        self.preOrderTraverse1(node.right)#每一次都是单独的一次调用函数

    def houxu(self,node):
        if not node:#为空时退出(出口)
            return None

        self.preOrderTraverse1(node.left)#压栈的方式是调用函数,弹栈的方式是return
        self.preOrderTraverse1(node.right)
        print(node.value)

#需要先执行的后压入栈中,有就压没有就不压
    def preOrderTraverse2(self,node):
        stack = [node]#栈是利用数组产生的,栈有的属性数组也有
        while len(stack) > 0:#栈用来存放任务,有时执行
            print(node.value)#先打印根节点
            if node.right:#将左右孩子压入栈中
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def preOrderTraverse3(self,node):
        stack = [node]#栈是利用数组产生的,栈有的属性数组也有
        while len(stack) > 0:#栈用来存放任务,有时执行
            pop_node = stack.pop()
            print(pop_node.value)#先打印根节点
            if pop_node.right:#将左右孩子压入栈中
                stack.append(pop_node.right)
            if pop_node.left:
                stack.append(pop_node.left)
            # node = stack.pop()


#每做完一个弹出
    #中序遍历,找到最左边的最底部,然后画三角
    def in_order_stack(self,node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left#先判断他有没有左节点
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)#打印根节点
                node = node.right#考虑右边节点
#后序遍历

    def post_order_stack(self,node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:#找出后序遍历的逆序放在stack1中
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:#将stack2中的元素出栈,即为结果
            print(stack2.pop().value,end=' ')
#层序遍历
    def level_order(self,root: Node):
        from queue import Queue
        if self.root is None:
            raise IndexError("empty tree")
        else:
            queue = Queue()
            queue.put(root)
            while not queue.empty():#用数组也可以
                node = queue.get()
                print(node.value)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(8,3,6,1)

    print(tree.preOrderTraverse3(tree.root))#或者不用初始化打印函数,打印tree.root