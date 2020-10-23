#逻辑上的结构,可以用数组或链表实现
class PriorityQueue:#就是根据大小决定优先级?那排个序
    def __init__(self):
        self.array = []
        self.size = 0


    def enqueue(self,val):#从尾部加入然后从下到上堆化
        self.array.append(val)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):

        child_index = self.size-1
        parent_index = (child_index-1) >> 1
        new = self.array[child_index]
        while child_index > 0 and new > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]
            child_index = parent_index
            parent_index = (child_index-1) >> 1
        self.array[child_index] = new

    def dequeue(self):#从头部删除然后从上到下堆化
        if self.size <= 0:
            raise Exception("空队列")
        remove_data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_data

    def heapify_down(self):
        # index = 0
        # max_index = index
        # while
        # if self.array[index*2+1] > self.array[max_index]:
        #     max_index = index*2+1
        # if self.array[index*2+2] > self.array[max_index]:
        #     max_index = index*2+2
        # if
        index = 0
        total_list = len(self.array) - 1
        while True:
            max_list = index
            if (index * 2 + 1) <= total_list and self.array[index * 2 + 1] > self.array[
                max_list]:
                max_list = index * 2 + 1
            if (index * 2 + 2) <= total_list and self.array[index * 2 + 2] > self.array[
                max_list]:
                max_list = index * 2 + 2
            if max_list == index:
                break#说明它已经是最大的,不用再看下面的
            self.array[index],self.array[max_list] = self.array[max_list],self.array[index]
            index = max_list


p = PriorityQueue()
p.enqueue(5)
p.enqueue(2)
p.enqueue(10)
p.enqueue(8)
p.enqueue(3)

print(p.array)
p.dequeue()
print(p.array)
