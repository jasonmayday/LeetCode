'''
冒泡排序(Bubble Sort)属于交换排序的一种。
基本的排序思路是：从头开始两两元素进行比较，大的元素就往上冒，这样遍历一轮后，最大的元素就会直接筛选出来。
然后再重复上述操作，即可完成第二大元素的冒泡。以此类推，直到所有的元素排序完成。

算法实现步骤：
    1. 比较相邻的元素，如果第一个比第二个大，就交换它们两个(确定排序规则：从小到大或从大到小)；
    2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对；
    3. 针对所有的元素重复以上的步骤，除了最后一个；
    4. 重复步骤1~3，直到没有任何一对元素需要比较，那么排序完成。
'''
from typing import List

def bubble_sort(arr: List[int]):
    n = len(arr) # n 为列表的长度
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j] # Python允许同时赋值。执行语句a, b = b, a，相当于同时执行两条赋值语句
 
if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    bubble_sort(arr)
    print("冒泡排序：", arr)