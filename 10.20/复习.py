# def reverse(nums):
#     if len(nums) <= 1:
#         return nums
#     head = 0
#     end = len(nums)-1
#     while head < end:
#         nums[head],nums[end] = nums[end],nums[head]
#         head += 1
#         end -= 1
#     return nums
#
# num = [5,2,0,1,3,1,4]
# reverse(num)#可以不return,但是就不是输出调用函数的结果,而是输出数组本身
# print(num)

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
#     def __repr__(self):
#         return f'Node({self.data})'
#
# def exchange(head):
#
#     dummy = Node(0)
#     dummy.next = head
#     pre = dummy
#
#     while pre.next and pre.next.next:
#
#         slow = pre.next
#         fast = pre.next.next
#         slow.next = fast.next
#         # pre.next = fast
#         fast.next = slow
#         pre.next = fast
#         pre = pre.next.next
#     return dummy.next
#
# def printNode(head):
#     curr = head
#     string = ""
#     while curr:
#         # for i in range(self.size)
#         string += f"{curr} -> "
#         curr = curr.next
#     return string + "END"
#
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
# node6 = Node(6)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
# print(printNode(exchange(node1)))

def threeSum(nums,target):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        head = i + 1
        end = len(nums) - 1
        while head < end:
            sumthree = nums[i] + nums[head] + nums[end]
            if sumthree < target:
                head += 1
            elif sumthree > target:
                end -= 1
            else:
                res +=  [[nums[i],nums[head],nums[end]]]
                while head < end and nums[head+1] == nums[head]:
                    head += 1
                while head < end and nums[end-1] == nums[end]:
                    end -= 1
                head += 1
                end -= 1
    return res

# num = [1,-1,0,3,-3,0,8,4,5,6]
# print(threeSum(num,0))
#
# def mergeTwo(num1,m,num2,n):
#     i = m-1
#     j = n-1
#     k = m+n-1
#     while i >= 0 and j >= 0:
#         if num1[i] > num2[j]:
#             num1[k] = num1[i]
#             i -= 1
#         else:
#             num1[k] = num2[j]
#             j -= 1
#         k -= 1
#     if j >= 0:
#         num1[:k+1] = num2[:j+1]
#     return num1
#
# num1 = [5,2,0,2,2,1]
# num2 = [1,3,1,4]
# print(mergeTwo(num1,6,num2),4)

#有效三角形的个数
# def triangle(nums):
#     nums.sort()
#     count = 0
#     for i in range(len(nums)-2):
#         head = i+1
#         end = len(nums)-1
#         while head < end:
#             if nums[i] + nums[head] > nums[end]:
#                 count += 1
#                 # head += 1
#                 end -= 1
#             elif nums[i] + nums[head] <= nums[end]:
#                 head += 1
#
#
#     return count

def triangle(nums):


    nums.sort()
    count = 0
    for i in range(len(nums)-1,1,-1):#也可以2,len(nums)这样遍历
        head = 0
        end = i-1
        while head < end:
            if nums[head] + nums[end] > nums[i]:
                count += (end-head)
                # head += 1
                end -= 1
            elif nums[head] + nums[end] <= nums[i]:
                head += 1


    return count

num = [2,2,3,4]
print(triangle(num))






