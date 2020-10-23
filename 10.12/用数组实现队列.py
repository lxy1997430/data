class Queue:
    def __init__(self):
        self.entries = []#记录
        self.size = 0

    def __repr__(self):
        printed = "<" + str(self.entries)[1:-1] + ">"
        return printed

    def enqueue(self,data):#入队
        self.entries.append(data)
        self.size += 1

    def dequeue(self):#出队
        temp = self.entries[0]
        self.entries = self.entries[1:]
        self.size -= 1
        return temp

    def front(self):
        return self.entries[0]

    def cap(self):
        return self.size

    def get(self,index):
        # for i in range(index):
        temp = self.entries[index]
        return temp

    def set(self,index,data):
        self.entries[index] = data

    def reverse(self):
        self.entries = self.entries[-1::-1]

e = Queue()
e.enqueue(5)
e.enqueue(2)
e.enqueue(0)
print(e.entries)
e.dequeue()
print(e.entries)
print(e.get(1))
