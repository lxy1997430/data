def remove(nums,value):#跟移除0一样
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == value:
            fast += 1
        else:
            nums[slow] = nums[fast]#先交换,因为不管你是0不是0都替换
            slow += 1
            fast += 1

    return slow

nums = [23,7,7,4,0,17,0,3,0,2]
print(remove(nums,7))