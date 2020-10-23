#不断地分区,直到不能再分,两个函数都分.
#双指针

def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(iList,start,end):#参数与递归函数主体对应
    pvriot = iList[start]#分区
    p = start + 1
    q = end
    while p <= q:#使最终初步排序完成
        while p <= q and iList[p] < pvriot:
            p += 1
        while p <= q and iList[q] >= pvriot:
            q -= 1
        if p < q:
            swap(iList,p,q)
    swap(iList,start,q)#最终p在第一个大于start的值,q在第一个小于start的值
    return q

def quickSort(iList,start,end):
    if start >= end:#出口
        return
    mid = partition(iList,start,end)#初步排序,分成三个区
    quickSort(iList,start,mid-1)#对左边的区再排序
    quickSort(iList,mid+1,end)
    return iList

#单指针
def partition2(iList,start,end):
    pivot = iList[start]#逆序时选第一个不太好,可以数组中随机选一个
    mark = start
    for i in range(start+1,end+1):#快指针去找比pivot小的
        if iList[i] < pivot:
            mark += 1
            iList[mark],iList[i] = iList[i],iList[mark]
    iList[start] = iList[mark]
    iList[mark] = pivot
    return mark

def quickSort2(iList,start,end):
    if start >= end:#出口
        return
    mark = partition(iList,start,end)#初步排序,分成三个区
    quickSort(iList,start,mark-1)#对左边的区再排序
    quickSort(iList,mark+1,end)
    return iList

num = [5,2,0,1,9,6]
print(quickSort2(num,0,5))




