from typing import List
class Node:#创建节点类
    def __init__(self,data,next=None):#节点类的属性
        self.data=data
        self.next=None

    def __repr__(self):#观察对象内容
        return 'Node({})'.format(self.data)

#链表指针后移的方法好像就是一直next,次数是看节点为不为空,而数组看下标,次数为不超过长度,
#链表操作节点时善于联系上下节点,尤其是上节点可以作为媒介和前进的标志,就是要注意节点记录和会不会有节点丢失或连接出错
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = Node(0)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
        #指针上岗
            slow = pre.next
            fast = pre.next.next
        #交换位置
            pre.next = fast
            slow.next = fast.next
            fast.next = slow
        #节点后移
            pre = pre.next.next
        return dummy.next




