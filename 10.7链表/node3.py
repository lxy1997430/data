class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self,index):
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr

    def insert(self,index,data):#不同情况的插入汇集
        new_node = Node(data)
        if index < 0 or index >self.size:#分析不同边界条件
            raise Exception('索引越界')

        elif self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev = self.get(index-1)
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def __repr__(self):
        curr = self.head
        string = ""
        while curr:
        # for i in range(self.size)
            string += f"{curr} -> "
            curr = curr.next
        return string + "END"

    def remove(self,index):
        if index < 0 or index > self.size:
            print('下标越界')
            exit()

        if index == 0:
            remove_node = self.head
            self.head = remove_node.next
            remove_node.next = None
        elif index == self.size-1:
            remove_node = self.tail
            prev = self.get(index-1)
            prev.next = None
            self.tail = prev
        else:
            remove_node = self.get(index)
            prev = self.get(index-1)
            prev.next = prev.next.next
            # remove_node = None加不加都行
        self.size -= 1

    def print_node(self):#打印链表里的值
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def reverse(self):
        pre = None
        curr = self.head
        for i in range(self.size):
            new_node = curr.next
            curr.next = pre
            pre = curr
            curr = new_node
        self.head = pre
        self.tail = self.get(self.size-1)




lk = LinkList()
lk.insert(0,1)
lk.insert(1,2)
lk.insert(2,3)
lk.insert(3,4)
lk.insert(4,5)
lk.remove(1)
# print(lk)
# lk.reverse()
print(lk)
# print(lk.find(0))
