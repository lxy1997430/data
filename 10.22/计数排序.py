#适合数值范围载某个区间内
def countSort(nums):
    res = list(range(max(nums)+1))
    a = []
    result = []
    for i in range(len(nums)):
        if nums[i] not in a:
            count = nums.count(nums[i])

        # if nums[i]
            res[nums[i]] = count
    for j in range(len(res)):
        result += [j]*res[j]
    return result
# num = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]
# print(countSort(num))

def count_sort(nums):
    max_value = max(nums)
    count_list = [0]*(max_value+1)
    for i in range(len(nums)):
        count_list[nums[i]] += 1
    sort_list = []
    for data in range(len(count_list)):
        for j in range(count_list[data]):
            sort_list.append(data)
    return sort_list

num = [9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9,7,9]
print(count_sort(num))