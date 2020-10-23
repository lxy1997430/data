'''
:author:long
:Create:2020/10/10 11:13
'''
class Node:#创建节点类
    def __init__(self,data,next=None):#节点类的属性
        self.data=data
        self.next=None

    def __repr__(self):#观察对象内容
        return 'Node({})'.format(self.data)



class Solution:
    def swapPairs(self, head,val):#使用虚拟节点,就不用每次都判断是否是头节点

        dummy = Node(1)
        dummy.next = head
        curr = dummy
        # head = dummy
        while curr.next:
            # 当前值等于目标值,跳过连接,指针不动
            if curr.next.data == val:
                temp = curr.next
                curr.next = curr.next.next
                temp.next = None
                #当前值不等于目标值,指针后移
            else:
                curr = curr.next
        return dummy.next#返回头结点,然后再根据头节点打印(链表的标志就是头节点,再找后续
def print_node(head):
    curr = head
    while curr:
        print(curr.data)
        curr = curr.next

 #只能用于直链表
node1 = Node(1)
node2 = Node(5)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
# string = ""
# for i in range(1,7):
#     string += node
s = Solution()
print_node(s.swapPairs(node1,5))







