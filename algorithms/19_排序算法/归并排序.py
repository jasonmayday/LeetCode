'''
归并排序(Merge Sort)是一种非常高效的排序方式，它用了分治的思想。
基本排序思想是：先将整个序列两两分开，然后每组中的两个元素排好序。
接着就是组与组和合并，只需将两组所有的元素遍历一遍，即可按顺序合并。
以此类推，最终所有组合并为一组时，整个数列完成排序。

算法实现步骤
    把长度为n的输入序列分成两个长度为n/2的子序列；
    对这两个子序列分别采用递归的进行排序；
    将两个排序好的子序列的元素拿出来，按照顺序合并成一个最终的序列，即可完成排序。
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
    print("归并排序：", arr)


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