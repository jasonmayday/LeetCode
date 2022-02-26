'''
希尔排序(Shell Sort)属于插入排序的一种，也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
其基本思想是：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）分别进行直接插入排序，
然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，再对全体元素进行一次直接插入排序。
因为直接插入排序在元素基本有序的情况下，效率是很高的，因此希尔排序在时间效率比直接插入排序有较大提高。

算法实现步骤
    选择一个增量序列 t1, t2, ..., tk，其中ti >tj, tk=1
    按增量序列个数k，对序列进行k 趟排序；
    每趟排序根据对应的增量$t_i$，将待排序列分割成若干长度为$m$的子序列，分别对各子序列进行直接插入排序。当增量因子为1 时，整个序列作为一个序列来处理，排序完成。
'''

from typing import List

def shell_sort(arr:List[int]):
    """
    希尔排序
    :param arr: 待排序的List
    :return: 希尔排序是就地排序(in-place)
    """
    length = len(arr)
    dist = length // 2
    
    while dist > 0:
        for i in range(dist, length):
            temp = arr[i]
            j = i
            while j >= dist and temp < arr[j-dist]:
                arr[j] = arr[j-dist]
                j -= dist
            arr[j] = temp
        dist //= 2

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    shell_sort(arr)
    print("希尔排序：", arr)