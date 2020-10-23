def removeDuplicats(nums):
    slow = 0
    fast = 1
    count = 1
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            count += 1
            if count == 2:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]
            fast += 1
            count = 1

    return slow + 1
num = [1,1,1,2,3,3,4,4,4,5]
removeDuplicats(num)


