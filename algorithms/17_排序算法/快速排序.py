'''
快速排序(Quick Sort)是对冒泡排序的一种改进。
其的基本思想: 选一基准元素，依次将剩余元素中小于该基准元素的值放置其左侧，大于等于该基准元素的值放置其右侧；
然后，取基准元素的前半部分和后半部分分别进行同样的处理；以此类推，直至各子序列剩余一个元素时，即排序完成（类比二叉树的思想)。

算法实现步骤
    首先设定一个分界值(pivot)，通过该分界值将数组分成左右两部分。
    将大于或等于分界值的数据集中到数组右边，小于分界值的数据集中到数组的左边。此时，左边部分中各元素都小于或等于分界值，而右边部分中各元素都大于或等于分界值,这个称为分区（partition）操作。
    然后，左边和右边的数据可以独立排序。对于左侧的数组数据，又可以取一个分界值，将该部分数据分成左右两部分，同样在左边放置较小值，右边放置较大值。右侧的数组数据也可以做类似处理。
    重复上述过程，通过递归（recursive）将左侧部分排好序后，再递归排好右侧部分的顺序。当左、右两个部分各数据排序完成后，整个数组的排序也就完成了。
'''
from typing import List

def partition(arr: List[int], low: int, high: int):
    pivot, j = arr[low], low
    for i in range(low + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[low], arr[j] = arr[j], arr[low]
    return j 

def quick_sort_between(arr: List[int], low: int, high: int):
    if high-low <= 1: # 递归结束条件
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

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    quick_sort(arr)
    print("快速排序：", arr)