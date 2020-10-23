class Stack:#以列表为基础的逻辑上的数据结构,而数组,链表是物理上存在的
    def __init__(self,size):
        self.stack = []
        self.size = 0

    def push(self,data):#压栈
        self.stack.append(data)
        self.size += 1

    def pop(self):#弹栈
        if self.stack:
            temp = self.stack.pop()
            self.size -= 1
        else:
            raise IndexError('pop from an empty stack')
        return temp#好好想需不需要返回值

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def sizeAll(self):
        return self.size

if __name__ == '__main__':
    s = Stack(10)
    for i in range(10):
        s.push(i)
    # print(s.stack)
    for i in range(5):
        s.pop()
    print(s.sizeAll())
    print(s.is_empty())
    print(s.peek())
