class Array:#用列表实现数组,没必要,强行实现,其他编程语言是数组,和列表类似
    def __init__(self,capacity):
        self.array = [None]*capacity
        self.size = 0

    def insert(self,index,element):#考虑好各种边界条件
        if index < 0 or index > self.size:#虽然可以插,但是不规范
            raise IndexError('下标越界')
        if self.size >= len(self.array):
        # if index >= len(self.array) or self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size-1,index-1,-1):
            self.array[i+1] = self.array[i]
        self.array[index] = element#写到循环外
        self.size += 1

    def remove(self,index):
        if index < 0 or index >= self.size:
            raise IndexError('数组越界')
        # if index >= len(self.array)
        for i in range(index,self.size):
            self.array[i] = self.array[i+1]
        self.size -= 1

    def addcapacity(self):
        #创建新数组
        new_array = [None]*len(self.array)*2#也可以for i in 数组
        #把旧数组的值放到新数组中
        for i in range(self.size):
            new_array[i] = self.array[i]
            #使用新数组
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i],end='\t')
arr = Array(5)
arr.insert(0,1)
arr.insert(3,2)
arr.insert(1,5)
arr.insert(2,4)
print(arr.array)
# arr.insert(2,100)
# print(arr.array)
arr.output()

