#给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
def threeSumClosest(nums,target):
    nums.sort()#为什么加了排序就好了
    res = {}
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                dis = abs(sum-target)
                res[dis] = sum
    result = [k for k, v in res.items()]

    return res[min(result)]
    # return res
#为什么排完序才可以用对撞指针
def threeSumClosest1(nums,target):
    nums, r, end = sorted(nums), float('inf'), len(nums) - 1
    for c in range(len(nums) - 2):
        i, j = max(c + 1, bisect.bisect_left(nums, target - nums[end] - nums[c], c + 1, end) - 1), end
        while r != target and i < j:
            s = nums[c] + nums[i] + nums[j]
            r, i, j = min(r, s, key=lambda x: abs(x - target)), i + (s < target), j - (s > target)
    return r

nums = [1,1,1,0]
print(threeSumClosest1(nums,-100))
# result = [k for k, v in threeSumClosest(nums,1).items()]
# print(result)
# result = threeSumClosest(nums,1)
# print(result.keys()[0])为什么这样不可以


#给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

def minSubArrayLen(s,nums):
    for i in range(1,len(nums)+1):
        for j in range(len(nums)):
            num = nums[j:j+i]
            dec = sum(num)
            if dec >= s:
                return len(num)
    return 0

# nums = [2,3,1,2,4,3]
# print(minSubArrayLen(7,nums))

#窗口滑动(可变滑动窗口,固定滑动窗口)
#先设置最小值然后覆盖
def minSubArrayLen(s,nums):
    left,sums,res = 0,0,float('inf')
    for right in range(len(nums)):
        sums += nums[right]
        while sums >= s:
            dis = right-left+1
            if dis < res:
                res = dis
            sums -= nums[left]
            left -= 1
    return 0 if res == float('inf') else res

#双指针
#while循环嵌套while循环
def minSubArrayLen1(s,nums):
    if s > sum(nums):
        return 0
    left, right, res, sum_lr = 0, 0, len(nums) + 1, 0  # 双指针都从第一位出发
    while right < len(nums):
        while sum_lr < s and right < len(nums):  # sum_lr小则右指针右移
            sum_lr += nums[right]
            right += 1
        while sum_lr >= s and left >= 0:  # sum_lr大则左指针右移
            res = min(res, right - left)
            sum_lr -= nums[left]
            left += 1
    return res

#二分查找
def minSubArrayLen2(s,nums):
    left, right, res = 0, len(nums), 0

    def helper(size):
        sum_size = 0
        for i in range(len(nums)):
            sum_size += nums[i]
            if i >= size:
                sum_size -= nums[i - size]
            if sum_size >= s:
                return True
        return False

    while left <= right:
        mid = (left + right) // 2  # 滑动窗口大小
        if helper(mid):  # 如果这个大小的窗口可以那么就缩小
            res = mid
            right = mid - 1
        else:  # 否则就增大窗口
            left = mid + 1
    return res

#二分法需要先排序?指针有时候也需要排序?



