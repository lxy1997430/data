#1,结合辗相除和更相减损法实现最大公约数求解
#把辗转相除法与更相减损术的优势结合起来，在更相减损术的基础上使用移位运算,把次数变少
#为什么不把位移和辗转相除结合
# def get_greatest_common_divisor(a,b):
#     small = min(a,b)
#     big = max(a,b)
#     if big%small == 0:
#         return small
#     if small%2 == 0 and big%2 == 0:
#         return 2*get_greatest_common_divisor(small >> 1, big >> 1)
#     elif small%2 != 0 and big%2 == 0:
#         return get_greatest_common_divisor(small >> 1,big)
#     elif small%2 == 0 and big%2 != 0:
#         return get_greatest_common_divisor(small >> 1, big)
#     else:
#         get_greatest_common_divisor(big-small,small)
#         get_greatest_common_divisor()


#给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#回文序列跟回文子串不一样asdhnbbaddjjhsd
# def longestPalindrome(s):
#     # res = []
#     for i in range(len(s)-1):
#         for j in range(len(s)-1,i,-1):
#             # if s[i] == s[j]:
#             if s[i:j+1] == s[j:i-1:-1]:
#
#
#                 return s[i:j+1]
#
# s = "babad"
#
# print(longestPalindrome(s))

#指针
# def longestPalindrome2(s):
#     head = 0
#     mid = 0
#     end = len(s)-1
#     while mid <= end:
#         if s[head:mid+1] == s[mid:head-1:-1]:
#             return s[head:mid+1]
#         else:
#             mid += 1
#
#     while mid >= head:
#         if s[mid:end+1] == s[end:mid-1:-1]:
#             return s[mid:end+1]
#         else:
#             end -= 1
#     while head < end:
#         if s[head:end+1] == s[end:head-1:-1]:
#             return s[head:end+1]
#         if s[head:end+1] != s[end:head-1:-1]:
#             head += 1
#         if s[head:end + 1] != s[end:head - 1:-1]:
#             end -= 1
#延伸
#求最大值,可以把所有数值都加到列表中,也可以if不断用大的更新小的
# #当函数特别复杂,循环多层嵌套时,可以考虑写成单独函数
def centerSpread(strs, left, right):#复杂度n的平方
    i = left
    j = right

    while i >=0 and j < len(strs):
        if strs[i] == strs[j]:
            i -= 1
            j += 1
        else:
            break
    return strs[i+1:j]

def longestPalindrome(strs):
    if len(strs) < 2:
        return strs
    res = strs[0]
    maxlen = 1
    for i in range(len(strs)-1):
        odd = centerSpread(strs,i,i)#反向走的指针
        even = centerSpread(strs,i,i+1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) > maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res
#
#
# s = "babad"
# print(longestPalindrome(s))
#荷兰旗,快排的基础
#给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#排序
# def sortColors(nums):
#     for i in range(1,len(nums)):
#         for j in range(len(nums)-i):
#             if nums[j] > nums[j+1]:
#                 nums[j],nums[j+1] = nums[j+1],nums[j]
#     return nums
#

# nums = [2,0,2,1,1,0]
#
# print(sortColors(nums))

# def sortColors1(nums):#不是原地
#     count0 = nums.count(0)
#     count1 = nums.count(1)
#     count2 = nums.count(2)
#     nums = count0*[0]+count1*[1]+count2*[2]
#     return nums

# def sortColors2(nums):
#     slow = 0
#     fast = 0
#     if nums[fast] == 0:

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         left, right, currIdx = 0, len(nums) - 1, 0
#         while currIdx <= right:
#             if nums[currIdx] == 0:
#                 nums[left], nums[currIdx] = nums[currIdx], nums[left]
#                 left += 1
#                 currIdx += 1
#             elif nums[currIdx] == 2:
#                 nums[right], nums[currIdx] = nums[currIdx], nums[right]
#                 right -= 1
#             else: # 1
#                 currIdx += 1

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         m=len(nums)
#         blue_num=0
#         j=0
#         for i in range(m):
#             if nums[i]==0:
#                 if i!=j:
#                     nums[j]=0
#                     nums[i]=1
#                 j+=1
#             elif nums[i]==2:
#                 blue_num+=1
#                 nums[i]=1
#         nums[m-blue_num:]=[2 for k in range(blue_num)]

def sortColors(nums):
    a = 0
    c = 0
    b = len(nums)-1
    while c <= b:
        if nums[c] == 0:
            nums[c],nums[a] = nums[a],nums[c]#a是色块01的边界,c是指针,b是色块12的边界
            c += 1
            a += 1
        elif nums[c] == 2:
            nums[c],nums[b] = nums[b],nums[c]
            b -= 1
        else:
            c += 1
