'''
插入排序(Insertion Sort)是一种简单直观的排序算法。

它的工作原理是：通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

算法实现步骤：
    1. 从第一个元素开始，该元素可以认为已经被排序；
    2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
    3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
    4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
    5. 将新元素插入到该位置后；
    重复步骤2~5。
'''
from typing import List

def insertion_sort(arr):
    for i in range(1, len(arr)):   # 从第二个元素开始比较，i表示当前的要插入的元素
        value = arr[i]
        j = i - 1
        # 把arr[i]插入到arr[0:i]中，arr[0:i]是有序的
        while j >= 0 and arr[j] > value:  # 如果满足条件,arr[j]就往后移
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = value   

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    insertion_sort(arr)
    print("插入排序：", arr)