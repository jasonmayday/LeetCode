'''
归并排序算法会把序列分成长度相同的两个子序列，当无法继续往下分时（也就是每个子序列中只有一个数据时），就对子序列进行归并。

归并指的是把两个排好序的子序列合并成一个有序序列。该操作会一直重复执行，直到所有子序列都归并为一个整体为止。

归并排序中，分割序列所花费的时间不算在运行时间内（可以当作序列本来就是分割好的）。

在合并两个已排好序的子序列时，只需重复比较首位数据的大小，然后移动较小的数据，因此只需花费和两个子序列的长度相应的运行时间。也就是说，完成一行归并所需的运行时间取决于这一行的数据量。

'''

def merge_sort(array):
    if len(array) == 1:  # 递归结束条件
        return array
    left_array = merge_sort(array[:len(array)//2])   # 使用二分法将数列分两个
    right_array = merge_sort(array[len(array)//2:])
    return merge(left_array, right_array)            # 使用递归运算
 
 
def merge(left_array, right_array):  # 合并操作，将两个有序数组 left[] 和 right[] 合并成一个大的有序数组
    left_index, right_index, merge_array = 0, 0, list()  # left 与 right 的下标指针
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            merge_array.append(left_array[left_index])
            left_index += 1
        else:
            merge_array.append(right_array[right_index])
            right_index += 1
    merge_array = merge_array + left_array[left_index:] + right_array[right_index:]
    return merge_array


if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    merge_sort(arr)
    print("选择排序：", arr)


'''
def merge_sort (lst):
    if len(lst)<=1:   #递归结束条件
        return lst
    #分解问题，并递归调用
    middle=len(lst)//2
    left=merge_sort(lst[:middle])
    right=merge_sort(lst[middle:])
    #合并左右部分，完成排序
    merged=[]
    while left and right:
        if left[0]<=right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left)
    return merged
'''