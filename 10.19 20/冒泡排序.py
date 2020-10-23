from randList import randList
# import random
def bubbleSort(nums):#大的放到最后
    if len(nums) <= 1:
        return nums
    for i in range(1,len(nums)):#控制轮数
        for j in range(len(nums)-i):#冒泡排序
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        print("第{}轮结束:" .format(i),end=' ')
        print(nums)
    return nums
# def randList():
#     List = []
#     for i in range(10):
#         List.append(random.randint(1,50))
#     return List
nums = randList.randList()#导的包要平齐,不要放在别的文件夹下
nums = bubbleSort(nums)
print(nums)

#优化
# def bubbleSort(nums):
#
#     for i in range(1,len(nums)):
#         flag = False
#         for j in range(len(nums)-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#                 flag = True
#         if flag == False:
#             break
#     return nums