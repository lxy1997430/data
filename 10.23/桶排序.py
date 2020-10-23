#桶排序主要是创建桶并把数据放入的过程,排序还是在桶内用其他排序方法
#一,创建桶,每个桶承载不同的范围.桶太少不好,尽量避免在桶里排序
#桶空间放桶
#二,
#量纲相近,身高,体重
def barketSort(nums):
    max_data = max(nums)
    min_data = min(nums)
    count_list = []
    cha = max_data - min_data
    count = len(nums)
    for i in range(count):
        count_list.append([])

    for i in range(len(nums)):
        num = int((nums[i]-min_data)*(count-1)/cha)
        count_list[num].append(nums[i])

    for iList in count_list:
        iList.sort()
    res = []
    for iList in count_list:
        for j in iList:
            res.append(j)

    return res

num = [4.5,0.84,3.25,2.18,0.5]
print(barketSort(num))



