两个区域,right区域是待排的牌,left是已经排好的牌,每次从未排的牌中拿出一张牌放到排好的牌中.类似玩扑克牌
def insertSort(iList):
    if len(iList) <= 1:
        return iList
    for right in range(1,len(iList)):
        target = iList[right]#右侧的第一个值
        for left in range(right):
            if target < iList[left]:
                iList[left+1:right+1] = iList[left:right]#整体后移,切片操作,相当于重新赋值,只有python有
                iList[left] = target
                break
    return iList
#
# iList = [5,2,0,2,2,1,1,9,9,6]
# print(insertSort(iList))

#待排序的要遍历,已排序的也要遍历
#为什么要重新在虚拟节点后面排序,因为链表没有索引,不好区分未排和已排
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)

def insertionSortList(head):
    dummy = Node(0)
    #创建一个新链表
    pre = dummy
    cur = head
    #遍历原列表
    while cur:#遍历待排序的节点
        temp = cur.next#记录下次查询的位置
        #对已排序好的链表进行遍历,找到待插入节点的位置
        while pre.next and pre.next.data < cur.data:
            pre = pre.next
        #已确定插入位置,完成插入
        cur.next = pre.next#安排后事
        pre.next = cur#处理前面节点

        #为下个节点的插入排序做准备
        cur = temp
        pre = dummy#必须从第一个开始遍历
    return dummy.next

def nodePrint(head):
    string = ""
    cur = head
    while cur:
        string += "{} --> ".format(cur)
        cur = cur.next
    return string + "end"

if __name__ == '__main__':
    node1 = Node(5)
    node2 = Node(2)
    node3 = Node(0)
    node4 = Node(1)
    node5 = Node(9)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    print(nodePrint(insertionSortList(node1)))















