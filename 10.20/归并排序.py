#分离指针(连接两个有序链表,数组)
#将无序数组一步步拆分成单个,再利用上述方法连接
#时间复杂度为O(nlogn)
# def merge(left,right):#python独有
#     res = []
#     while left and right:
#         if left[0] > right[0]:
#             res.append(right.pop(0))
#         else:
#             res.append(left.pop(0))
#     if left:
#         res.extend(left)
#     if right: b
#         res.extend(right)
#     return res
#指针
def merge(left,right):#通用
    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            res.append(right[j])
            j += 1
        else:
            res.append(left[i])
            i += 1
    # if i < len(left):
        res.extend(left[i:])
    # if j < len(right):
        res.extend(right[j:])
    return res


def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) >> 1
    left,right = nums[:mid],nums[mid:]
    return merge(mergeSort(left),mergeSort(right))

num = [5,2,0,1,9,6,8,4]
print(mergeSort(num))