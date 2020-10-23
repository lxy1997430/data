# 数组实现二分查找(有序数组)
#对撞指针
#做算法时尽量不要用函数


# def binarySearch1(nums,val):
#     left = 0
#     right = len(nums) - 1
#     while left < right:#还可以加=
#         if nums[left] == val:
#             return left
#         elif nums[right] == val:
#             return right
#         else:
#             mid = (left + right) // 2
#             if nums[mid] > val:
#                 right = mid
#             elif nums[mid] < val:
#                 left = mid
#             else:
#                 return mid

# def binarySearch2(nums,val):
#     left = -1
#     right = len(nums)
#     while left <= right:#还可以加=
#         mid = (left + right) // 2
#         if nums[mid] > val:
#             right = mid
#         elif nums[mid] < val:
#             left = mid
#         else:
#             return mid


# def binarySearch3(nums, val):
#     left = -1
#     right = len(nums)
#     while left <= right:  # 还可以加=
#         # mid = (left + right) // 2
#         mid = left + (right - left)//2#适用于其他编程语言
#         if nums[mid] > val:
#             left = mid
#         elif nums[mid] < val:
#             right = mid
#         else:
#             return mid


#递归
# def binarySearch4(nums,val,left,right):
#     if right > 0:
#         mid = left + (right - left) // 2
#         if nums[mid] == val:
#             return mid
#         elif nums[mid] > val:
#             return binarySearch4(nums,val,left,mid-1)
#         else:
#             return binarySearch4(nums,val,mid+1,right)
#     else:
#         return -1
# nums = [1,2,3,4,5,6,7]
# print(binarySearch4(nums,10,0,len(nums)-1))
# 翻转数组
#指针
#数组跟列表使用时不区分?
def reverse(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    return nums

nums = [5,2,0,1,3,1,4]
print(reverse(nums))





# 88合并两个有序数组
#只能在num1的基础上
#自己的方法,类比连接两个链表
# def hebing(num1,num2):
#     head1 = 0
#     head2 = 0
#     result = []
#     temp = 0
#     while head1<len(num1) and head2<len(num2):
#         if num1[head1]<num2[head2]:
#             temp=num1[head1]
#             result.append(temp)
#             head1+=1
#         else:
#             temp=num2[head2]
#             result.append(temp)
#             head2+=1
#         if head1=len(num1):
#             result+=num2[head2:]
#     return result

def mergeTwo(num1,m,num2,n):
    i = m-1
    j = n-1
    k = m + n - 1#控制输出数组的大小,结果数组的最后一个索引
    while i >= 0 and j >= 0:
        if num1[i] >= num2[j]:#从后往前避免有数据丢失
            num1[k] = num1[i]
            i -= 1
        else:
            num1[k] = num2[j]
            j -= 1
        k -= 1
    while i >= 0:
        num1[k] = num1[i]
        i -= 1
        k -= 1
    while j >= 0:
        num1[k] = num2[j]
        j -= 1
        k -= 1
    return num1
