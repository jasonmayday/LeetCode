'''
基数排序(Radix Sort)是一种非比较型整数排序算法，是桶排序的扩展。
基本思想是：将所有待比较数值统一为同样的数位长度，数位较短的数前面补零。
按照低位先排序，分别放入10个队列中，然后采用先进先出的原则进行收集；再按照高位排序，然后再收集；依次类推，直到最高位，最终得到排好序的数列。
对于数值偏小的一组序列，其速度是非常快的，时间复杂度达到了线性，而且思想也非常的巧妙。

算法实现步骤
    取得数组中的最大数，并取得位数；
    对数位较短的数前面补零；
    分配，先从个位开始，根据位值(0-9)分别放到0~9号桶中;
    收集，再将放置在0~9号桶中的数据按顺序放到数组中;
    重复3~4过程，直到最高位，即可完成排序。

'''

from typing import List

def radix_sort(arr:List[int]):
    n = len(str(max(arr)))  # 记录最大值的位数
    for k in range(n):#n轮排序
        # 每一轮生成10个列表
        bucket_list=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        for i in arr:
            # 按第k位放入到桶中
            bucket_list[i//(10**k)%10].append(i)
        # 按当前桶的顺序重排列表
        arr=[j for i in bucket_list for j in i]
    return arr

if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    radix_sort(arr)
    print("基数排序：", arr)