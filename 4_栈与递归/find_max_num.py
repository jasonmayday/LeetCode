'''
找出列表中最大的数字。
'''

def max(arr):
    if arr  == []:    # 基线条件：数组为空
        return None
    elif len(arr) == 1:    # 基线条件：数组内只有一个元素
        return arr[0]
    elif len(arr) == 2:    # 基线条件：数组内有两个元素，返回最大值（可用内置的max()代替）
        if arr[0] > arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        return max([arr[0], max(arr[1:])])    # 递归条件：比较第一个元素与数组中剩余元素的最大值
