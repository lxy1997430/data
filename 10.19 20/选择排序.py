import random
def selectionSort(nums):
    if len(nums) <= 1:
        return nums
    for i in range(len(nums)-1):#控制轮数
        min_index = i
        for j in range(i+1,len(nums)):#找到最小值对应的索引
            if nums[min_index] > nums[j]:
                min_index = j
        nums[i],nums[min_index] = nums[min_index],nums[i]#只交换一步
        # print("第{}轮结束".format(i+1),end=' ')
        # print(nums)
    return nums

def randList():
    List = []
    for i in range(10):
        List.append(random.randint(1,50))
    return List

nums = randList()
num = selectionSort(nums)
print(num)