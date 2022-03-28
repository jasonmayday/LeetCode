'''
快速排序(Quick Sort)是对冒泡排序的一种改进。
基本思想: 选一基准元素，依次将剩余元素中小于该基准元素的值放置其左侧，大于等于该基准元素的值放置其右侧；
然后，取基准元素的前半部分和后半部分分别进行同样的处理；以此类推，直至各子序列剩余一个元素时，即排序完成（类比二叉树的思想)。

算法实现步骤
    首先设定一个分界值(pivot)，通过该分界值将数组分成左右两部分。
    将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。此时，左边部分中各元素都小于或等于分界值，而右边部分中各元素都大于或等于分界值,这个称为分区（partition）操作。
    然后，左边和右边的数据可以独立排序。对于左侧的数组数据，又可以取一个分界值，将该部分数据分成左右两部分，同样在左边放置较小值，右边放置较大值。右侧的数组数据也可以做类似处理。
    重复上述过程，通过递归（recursive）将左侧部分排好序后，再递归排好右侧部分的顺序。当左、右两个部分各数据排序完成后，整个数组的排序也就完成了。
'''

from typing import List

# 解法1：
def partition(arr: List[int], low: int, high: int):
    pivot, j = arr[low], low
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort_between(arr: List[int], low: int, high: int):
    if high - low <= 1: # 递归结束条件
        return

    m = partition(arr, low, high)  # arr[m] 作为划分标准
    quick_sort_between(arr, low, m - 1)
    quick_sort_between(arr, m + 1, high)

def quick_sort(arr:List[int]):
    """
    快速排序(in-place)
    :param arr: 待排序的List
    :return: 快速排序是就地排序(in-place)
    """
    quick_sort_between(arr,0, len(arr) - 1)


# 解法2：
def quick_sort(arr):
    if len(arr) <= 1:    # 边界条件
        return arr
    else:
        pivot = arr[len(arr) // 2]              # 取数组的中间的数为基准数
    left = []
    right = []
    middle = [pivot]             # 定义空列表，分别存储小于/大于/等于基准数的元素
    for i in range(1, len(arr)): # 遍历数组，把元素归类到3个列表中
        if arr[i] > pivot:
            right.append(arr[i])
        elif arr[i] < pivot:
            left.append(arr[i])
        else:
            middle.append(arr[i])
    return quick_sort(left) + middle + quick_sort(right) #对左右子列表快排，拼接3个列表并返回


# 解法3：
def quick_sort_3(arr:List[int], start, end):
    if start >= end:    # 递归的退出条件
        return
    mid = arr[start]    # 设定起始元素为要寻找位置的基准元素
    low = start         # low为序列左边的由左向右移动的游标
    high = end          # high为序列右边的由右向左移动的游标
    while low < high:
        while low < high and arr[high] >= mid:  # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
            high -= 1
        arr[low] = arr[high]                   # 将high指向的元素放到low的位置上

        while low < high and arr[low] < mid:    # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
            low += 1
        arr[high] = arr[low]                   # 将low指向的元素放到high的位置上
    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    arr[low] = mid                  # 将基准元素放到该位置
    quick_sort_3(arr, start, low-1)   # 对基准元素左边的子序列进行快速排序
    quick_sort_3(arr, low+1, end)     # 对基准元素右边的子序列进行快速排序

def quick_sort(arr, l, r):
            if l >= r: return   # 子数组长度为 1 时终止递归
            i, j = l, r     # 初始化哨兵索引位置（以 arr[l] 作为基准数）
            while i < j:    # 循环交换，两哨兵相遇时跳出
                while i < j and arr[j] >= arr[l]:   # 从右向左，查抄首个小于基准数的元素
                    j -= 1
                while i < j and arr[i] <= arr[l]:   # 从左向右，查抄首个大于基准数的元素
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]     # 交换arr[i] 和 arr[j]
            arr[l], arr[i] = arr[i], arr[l]     # 交换基准数 arr[l] 和 arr[i]
            # 哨兵划分操作完成后，左子数组所有数字 ≤ 基准数，右子数组所有数字 ≥ 基准数
            quick_sort(arr, l, i - 1)   # 递归左（右）子数组执行哨兵划分
            quick_sort(arr, i + 1, r)

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    quick_sort(arr)
    print("快速排序：", arr)