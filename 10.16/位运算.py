# import time
# def xiaoyi(n):
#
#     count = 0
#     while n != 0:
#         n = n&(n-1)
#         count += 1
#     return count
#
# print(xiaoyi(10))
#
# def singleNumber(nums: List):#异或满足交换律和结合律,不用排序
#     res = 0
#     for i in nums:
#         res = res^i
#     return res
def totalHammingDistance(nums):
    sum = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            count = 0
            n = nums[i] ^ nums[j]
            while n != 0:
                n = n & (n - 1)
                count += 1
            sum += count
    return sum
nums = [4,14,2]
print(totalHammingDistance(nums))

def gongyueshu(x,y):
    i = 1
    res = []
    while i<=x:
        if x%i == 0 and y%i == 0:
           res += [i]
        i += 1
    return max(res)

print(gongyueshu(5,3))

def get_greatest_common_divisor(a,b):
    small = min(a,b)
    big = max(a,b)
    if big%small == 0:
        return small
    for i in range(small//2,0,-1):
        if small%i == 0 and big%i == 0:
            return i
print(get_greatest_common_divisor(15,9))

辗转相除法,两个正整数的最大公约数等于等于余数和较小数的公约数
def get_greatest_common_divisor1(a,b):
    small = min(a,b)
    big = max(a,b)
    if big%small == 0:
        return small
    return get_greatest_common_divisor1(small,big%small)
print(get_greatest_common_divisor1(15,9))
更相减损法,两个正整数a,b的最大公约数等于a-b的差c和b之间的最大公约数
def get_greatest_common_divisor2(a,b):#辗转相除法次数更少,但是计算机不适合乘除尤其取余,更适合移位
#两个数都比较大时取余麻烦,两个数相差较大时减法次数多

    small = min(a,b)
    big = max(a, b)
    if big % small == 0:
        return small
    return get_greatest_common_divisor2((big-small),small)

start = time.time()
print(get_greatest_common_divisor2(15,9))
end = time.time()
print(end-start)

两者结合,两个都有,不同情况用不同的方法