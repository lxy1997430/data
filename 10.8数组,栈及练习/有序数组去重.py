class Solution:#快慢指针#直接赋值,不用移动数据,将重复的值都到最后(不放是不是也行)
    def removeDuplicated(self,nums):#慢指尖不动,快指针去寻找和它不同的
        fast = 1
        slow = 0
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
            else:
                fast += 1
        return slow + 1#如果要返回数组就切片吗

# 时间长,占用内存大
    # def quchong(nums):
    #     for i in range(len(nums)):
    #         for j in range(len(nums)-1,i,-1):
    #             if nums[j] == nums[i]:
    #                 nums[j] = nums[j+1]
