class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
   #判断环的函数不是类函数,不能写self
def isCircle(head: Node) -> bool:#类型注解,执行的时候会被忽略,只需要传入链表头部
    fast = head
    slow = head
    while fast and fast.next:#保证奇数偶数都不为空,以及空没有next属性
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False

def circleIndex(head: Node):
    fast = head
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    slow = head
    while slow != fast:
    # while slow and slow.next:
        slow = slow.next
        fast = fast.next
        # if slow == fast:

            # return slow
    return slow



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

