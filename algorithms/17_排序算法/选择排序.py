'''
1. 设第一个元素为比较元素，依次和后面的元素比较，比较完所有元素找到最小的元素，将它和第一个元素互换
2. 重复上述操作，我们找出第二小的元素和第二个位置的元素互换，以此类推找出剩余最小元素将它换到前面，即完成排序
'''

"""选择排序"""

def selection_sort(arr):
    for i in range(len(arr)):  # 第一层for表示循环选择的遍数
        min_index = i              # 将起始元素设为最小元素
        min_val = arr[i]
        for j in range(i, len(arr)):  # 第二层for表示最小元素和后面的元素逐个比较
            if arr[j] < min_val:   # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_val = arr[j]
                min_index = j             # 查找一遍后将最小元素与起始元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    selection_sort(arr)
    print("选择排序：", arr)