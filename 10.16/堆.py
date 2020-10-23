class Heap:
    def __init__(self):
        self.data_list = []#用列表实现,列表也可以存树,列表的下标和树的下标一一对应,本质是完全二叉,实体是数组树

    def get_parent_index(self,index):
        if index == 0 or index > len(self.data_list) - 1:#向下取整
            return None
        else:
            return (index-1) >> 1#位运算比较快

    def swap(self,index_a,index_b):
        self.data_list[index_a],self.data_list[index_b] = self.data_list[index_b],self.data_list[index_a]

    def insert(self,data):
        #先把元素放在最后,然后从后往前依次堆化(最大堆)

        self.data_list.append(data)
        index = len(self.data_list)-1

        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[index] > self.data_list[parent]:#parent的判断要放在前面
            self.swap(index,parent)
            index = parent#节点上移
            parent = self.get_parent_index(index)#再次寻找父节点

    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self,index):#从上到下堆化,保持最大值在顶部

        total_list = len(self.data_list)-1
        while True:
            max_list = index  #先定义一个最大值
            if (index*2+1) <= total_list and self.data_list[index*2+1] > self.data_list[max_list]:#从它和左右孩子中找出最大值,但是要先判断是否有左右孩子
                max_list = index*2+1
            if (index*2+2) <= total_list and self.data_list[index*2+2] > self.data_list[max_list]:#从它和左右孩子中找出最大值,但是要先判断是否有左右孩子
                max_list = index*2+2
            if max_list == index:
                break
            self.swap(max_list,index)
            index = max_list

if __name__ == '__main__':
    h = Heap()
    h.insert(1)
    h.insert(2)
    h.insert(3)
    h.insert(4)
    print(h.data_list)
