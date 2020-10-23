from typing import List
class Node:#创建节点类
    def __init__(self,data,next=None):#节点类的属性
        self.data=data
        self.next=None

    def __repr__(self):#观察对象内容
        return 'Node({})'.format(self.data)


class LinkedList:#创建链表类,与节点类并列,要用到节点类(要素),增删改查等方法在链表类定义
    def __init__(self):#链表的属性:头部
        self.head=None

    def __repr__(self):#将链表以字符串形式输出
        current = self.head
        str = ""
        while current:
            str += "{} --> ".format(current)#这里的current代表节点,在节点类中已经执行了打印操作
            current = current.next
        return str + "end"

    def insert_head(self,data):#在头部插入
        new_node=Node(data)#建立一个新节点
        if self.head:
            new_node.next=self.head#指向头部串在一起
        self.head=new_node#更新头部

    def append(self,data):#从尾部插入
        if self.head:
            temp = self.head
            while temp.next:#遍历链表
                temp = temp.next
            temp.next = Node(data)
        else:
            self.insert_head(data)
    def insert(self,i,data):#任意位置插入节点
        if self.head is None:#如果链表为空
            self.insert_head(data)
        elif i == 1:
            self.insert_head(data)
        else:
            curr = self.head
            pre = curr
            j = 1
            while j < i:
                pre = curr
                curr = curr.next
                j += 1
            node = Node(data)
            pre.next = node
            node.next = curr
    def linklist(self,object: List) -> None:
        self.head = Node(object[0])
        temp = self.head
        for i in object[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def delete_header(self):
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        #不用return也可以
    def delete_end(self):
        temp = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None

        else:
            return "是空链表"

    def reverse(self):
        pre = None#记录前一个,当前,后一个
        curr = self.head
        while curr:
            next_node = curr.next#向右看
            curr.next = pre#向后转
            pre = curr#齐步走
            curr = next_node
        # while curr:#一定要先记录当前的下一个,不然断开之后就找不到了
        #     curr.next = pre
        #     pre = curr
        #     curr = curr.next
        self.head = pre

    def __getitem__(self, index):
        curr = self.head
        if curr is None:
            raise IndexError("The Linked List is empty")

        for _ in range(1,index):
            if curr.next is None:

                raise IndexError("Index out of range.")
            curr = curr.next
        return curr

    def get(self,index):
        self.__getitem__(index)

    def __setitem__(self, index, data):
        curr = self.head
        if curr is None:
            raise
        for _ in range(1,index):
            if curr.next is None:
                raise
            curr = curr.next
        curr.data = data

    def set(self,index,data):
        self.__setitem__(index,data)
# link = LinkedList()
# link.append(2)
# link.append(3)
# link.insert_head(0)
# link.insert(2,8)
# print(link)
list = [1,2,3,4,5,6]
linkk = LinkedList()
linkk.linklist(list)
print(linkk)
linkk.reverse()
print(linkk)
print(linkk.__getitem__(1))

