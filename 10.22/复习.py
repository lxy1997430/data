# def merge(left, right):
#     res = []
#     while left and right:
#         if left[0] < right[0]:
#             res.append(left.pop(0))
#
#         else:
#             res.append(right.pop(0))
#     if left:
#         res.extend(left)
#     if right:
#         res.extend(right)
#     return res
#
# def merge2(left,right):
#     res = []
#     i = 0
#     j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     if i <len(left):
#         res.extend(left[i:])
#     if j < len(right):
#         res.extend(right[j:])
#     return res
#
# def mergeSort(nums):
#     if len(nums) <= 1:
#         return nums
#     mid = len(nums) >> 1
#     left = nums[:mid]
#     right = nums[mid:]
#     return merge(mergeSort(left),mergeSort(right))

# def swap(array,a,b):
#     array[a],array[b] = array[b],array[a]
#
# def partition(iList,start,end):#参数与递归函数主体对应
#     pvriot = iList[start]#分区
#     p = start + 1
#     q = end
#     while p <= q:#使最终初步排序完成
#         while p <= q and iList[p] < pvriot:
#             p += 1
#         while p <= q and iList[q] >= pvriot:
#             q -= 1
#         if p < q:
#             swap(iList,p,q)
#     swap(iList,start,q)#最终p在第一个大于start的值,q在第一个小于start的值
#     return q
#
# def quickSort(iList,start,end):
#     if start >= end:#出口
#         return
#     mid = partition(iList,start,end)#初步排序,分成三个区
#     quickSort(iList,start,mid-1)#对左边的区再排序
#     quickSort(iList,mid+1,end)
#     return iList
#
# num = [5,2,0,1,9,6]
# print(quickSort(num,0,5))

def quchong(nums):
    nums.sort()
    fast = 1
    slow = 0
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
    # return slow + 1
    return nums[:slow+1]
def removeZeros(nums):
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]
            slow += 1
            fast += 1
    for i in range(slow,fast):
        nums[i] = 0
    return nums

num = [5,2,0,2,2,1,9,9,6,1,2,1,8,4,8,8]
num2 = [5,2,0,2,0,1]
print(quchong(num))
# print(quchong(num))
print(removeZeros(num2))