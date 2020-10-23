class Node:#创建节点类
    def __init__(self,data,next=None):#节点类的属性
        self.data=data
        self.next=None

    def __repr__(self):#观察对象内容
        return 'Node({})'.format(self.data)
#归并排序
# def lianjie(l1,l2):
#     dummy = Node(0)
#     curr = dummy
#     if l1 is None:
#         curr.next = l2
#         # 会一直连下去
#     if l2 is None:
#         curr.next = l1
#
#     while l1 or l2:
#
#         if l1.data >= l2.data:
#             curr.next = Node(l2.data)#增加了空间复杂度
#             l2 = l2.next
#
#         else:
#             curr.next = Node(l1.data)
#             l1 = l1.next
#         curr = curr.next
#
#
#     return dummy.next


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
def printNode(head):
    curr = head
    while curr:
        print(curr,end=' ')
        curr = curr.next

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
node10 = Node(1)
node20= Node(2)
node30= Node(3)
node40= Node(4)

node10.next = node20
node20.next = node30
node30.next = node40

printNode((lianjie(node1,node10)))
