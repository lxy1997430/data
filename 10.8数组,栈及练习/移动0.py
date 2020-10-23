# class Solution:
def moveZero(nums):#慢指针不动,快指针去找不为0的
    fast = 0
    slow = 0
    while fast < len(nums):
        if nums[fast] == 0:
            fast += 1
        else:
            nums[slow] = nums[fast]#先交换,因为不管你是0不是0都替换
            slow += 1
            fast += 1
    for i in range(slow,len(nums)):#fast往前移到了None,slow也往前多移一格
        nums[i] = 0
    return nums

   #时间长,占用内存大
    # def movezero(self):
    #     for i in range(self.size-1,-1,-1):
    #         if self.array[i] == 0:
    #             for j in range(i,self.size-1):
    #                 self.array[j] = self.array[j+1]
    #             self.array[self.size-1] = 0
# s = Solution()
nums = [23,7,7,4,0,17,0,3,0,2]
print(moveZero(nums))#一定要有返回值,不然没有结果