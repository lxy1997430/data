# def lianjie(l1,l2):
#     dummy = Node(0)
#     curr = dummy
#     while l1 or l2:
#         if l1.data <= l2.data:
#             curr.next = Node(l1.data)
#             l1 = l1.next
#
#         else:
#             curr.next = Node(l2.data)
#             l2 = l2.next
#         curr = curr.next
#         if l1 is None:
#             curr.next = l2
#             break
#         if l2 is None:
#             curr.next = l1
#             break
#      return dummy.next

class Node:#创建节点类
    def __init__(self,data,next=None):#节点类的属性
        self.data=data
        self.next=None

    def __repr__(self):#观察对象内容
        return 'Node({})'.format(self.data)

def lianjie(l1, l2):
    dummy = Node(0)
    curr = dummy
    while l1 and l2:
        if l1.data <= l2.data:
            curr.next = Node(l1.data)
            l1 = l1.next

        else:
            curr.next = Node(l2.data)
            l2 = l2.next
        curr = curr.next
    if l1 is None:
            curr.next = l2

    if l2 is None:
            curr.next = l1

    return dummy.next
#数组实现栈
class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self,element):

        self.stack.append(element)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError('pop from empty stack')
        else:
            temp = self.stack.pop()#默认删除最后一个值并返回该值
            self.size -= 1
        return temp
    def peek(self):
        if self.stack:
            return self.stack[-1]


class Stack:


if __name__ == '__main__':#函数执行的入口
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node1
    print(isCircle(node1))
    print(circleIndex(node1))