def sum(arr):
    if arr  == []:    # 基线条件：数组为空
        return 0
#    elif len(arr) == 1:    # 基线条件：数组内只有一个元素(可省略)
#        return arr[0]
    else:
        return arr[0] + sum(arr[1:])

print (sum([1,2,3,4,5]))