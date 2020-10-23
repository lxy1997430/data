两数之和
暴力循环,时间复杂度O(n^2)
def twoSum(nums,target):

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):

            if nums[j] == target - nums[i]:
                return ([i,j])

nums = [2,7,11,15]
print(twoSum(nums,9))

#有序(对撞指针)
#只能获取值

def twoSum(nums, target):
    nums.sort()#快排,时间复杂度为O(nlogn),排完序后下标会变
    head = 0
    end = len(nums)-1
    while head < end:
        sum = nums[head] + nums[end]
        if sum == target:
            print([head,end])
            head += 1
            end -= 1
        else:
            if sum < target:
                head += 1
            else:
                end -= 1
#
# nums = [2,7,11,15]
# twoSum(nums,9)

#用空间换取时间,硬件成本低,存放遍历出的值和下标
def twoSum(nums, target):
    nums_dict = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp in nums_dict:
            print(i,nums_dict[temp])
        else:
            nums_dict[nums[i]] = i
#
# nums = [2,7,11,15]
# twoSum(nums,9)


#无序

#三数之和
#先固定一个,然后另外两个对撞指针

#暴力方式,不好
def threeSum(nums):
    first = 0
    second = 1
    third = 2
    result = []
    while first < len(nums)-2:
        while second < len(nums)-1:
            while third < len(nums):
                if nums[first]+nums[second]+nums[third]==0:
                    result.append([nums[first],nums[second],nums[third]])
                    third+=1
    return result#超过时间限制

num = [0,1,-1,2,3,4]
print(threeSum(num))

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):#优化,为了去重
        if i>0 and nums[i]==nums[i-1]:
            continue

        head = i+1
        end = len(nums)-1

        while head<end:
            if nums[i]+nums[head]+nums[end] == 0:
                # res.append([nums[i],nums[head],nums[end]])
                res+=[[nums[i],nums[head],nums[end]]]
                while head<end and nums[head+1] == nums[head]:
                    head+=1
                while head<end and nums[end-1]==nums[end]:
                    end-=1
                head+=1
                end-=1
            elif nums[i]+nums[head]+nums[end] < 0:
                head+=1
            else:
                end-=1
    return res




