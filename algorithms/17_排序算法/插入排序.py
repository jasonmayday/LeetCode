
from typing import List

def insertion_sort(arr):
    for i in range(1, len(arr)):   # 从第二个元素开始比较，i表示当前的要插入的元素
        key = arr[i]
        j = i - 1
        # 把arr[i]插入到arr[0:i]中，arr[0:i]是有序的
        while j >= 0 and arr[j] > key:  # 如果满足条件,arr[j]就往后移
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = key   

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    insertion_sort(arr)
    print("插入排序：", arr)