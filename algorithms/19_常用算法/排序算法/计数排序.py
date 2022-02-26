'''
计数排序(Counting Sort)不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
它的基本思想是：给定的输入序列中的每一个元素x，确定该序列中值小于等于x元素的个数，然后将x直接存放到最终的排序序列的正确位置上。

算法实现步骤
    根据待排序集合中最大元素和最小元素的差值范围，申请额外空间；
    遍历待排序集合，将每一个元素出现的次数记录到元素值对应的额外空间内；
    对额外空间内数据进行计算，得出每一个元素的正确位置；
    将待排序集合每一个元素移动到计算得出的正确位置上。

'''
# counting_sort 代码实现

from typing import List
    
def counting_sort(arr:List[int]):
    max=min=0
    for i in arr:
        if i < min:
            min = i
        if i > max:
            max = i 
    count = [0] * (max - min +1)
    for j in range(max-min+1):
        count[j]=0
    for index in arr:
        count[index-min]+=1
    index=0
    for a in range(max-min+1):
        for c in range(count[a]):
            arr[index]=a+min
            index+=1

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    counting_sort(arr)
    print("计数排序：", arr)