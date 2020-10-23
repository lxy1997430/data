class Node:
    def __init__(self,data,next=None):
        self.data: Any = data
        self.next: Optional[None] = None

    def __repr__(self):
        return 'Node({})'.format(self.data)


class LinkedList:
    def __init__(self) -> NoReturn:
        self.top = None#只是一个记号,但是不能用尾部,因为反过来方向不对

    def __repr__(self):
        temp = self.top
        str = ""
        while temp:
            str += "{} --> ".format(temp)
            temp = temp.next
        return str + 'End'

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.size += 1#为什么这里不需要返回值

    def pop(self):
        if self.top is None:
            raise IndexError('pop from ')
        else:
            node = self.top
            self.top = node.next
            node.next = None
            self.size -= 1
            return node



