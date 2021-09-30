'''
编写一个递归函数来计算列表包含的元素数。
'''

def count(arr):
    if arr  == []:    # 基线条件：数组为空
        return 0
#    elif len(arr) == 1:    # 基线条件：数组内只有一个元素(可省略)
#        return 1
    else:
        return 1 + count(arr[1:])    # 递归条件：计算数组中第一个元素外剩余元素个数，再加一

print (count([1,2,3,4,5]))