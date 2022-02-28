'''
快速排序，是使用递归的一种排序
'''


array = [10, 5, 2, 3, 42, 12, 23, 31, 8, 17, 27]

def quicksort(array):
    if len(array) < 2:
        return array        # 基线条件：为空或只包含一个元素的数组是“有序”的
    else:
        pivot = array[0]    # 递归条件, 取数组中第一个数为基准值

        less = [i for i in array[1:] if i <= pivot]   # less为所有小于基准值的元素组成的子数组

        greater = [i for i in array[1:] if i > pivot] # greater为所有大于基准值的元素组成的子数组
        
        return quicksort(less) + [pivot] + quicksort(greater) # 递归，直到数组数量小于2
    
print (quicksort(array))