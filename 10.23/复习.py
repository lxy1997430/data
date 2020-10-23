#插入排序
def insertSort(nums):
    for right in range(1,len(nums)):
        temp = nums[right]
        for left in range(right):
            if nums[right] < nums[left]:
                nums[left+1:right+1] = nums[left:right]
                nums[left] = temp
                break
    return nums



def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(iList,start,end):
    pvriot = iList[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and iList[p] < pvriot:
            p += 1
        while p <= q and iList[q] >= pvriot:
            q -= 1
        if p < q:
            swap(iList,p,q)
    swap(iList,start,q)
    return q

def quickSort(iList,start,end):
    if start >= end:
        return
    mid = partition(iList,start,end)
    quickSort(iList,start,mid-1)
    quickSort(iList,mid+1,end)
    return iList

num = [5,2,0,1,9,6,4,8]
print(quickSort(num,0,len(num)-1))