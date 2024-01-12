
""" Partition函数
    首先，先写partition模板 """
def partition(nums, left, right):
    pivot = nums[left]#初始化一个待比较数据
    i,j = left, right
    while(i < j):
        while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
            j-=1
        nums[i] = nums[j] #将更小的数放入左边
        while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
            i+=1
        nums[j] = nums[i] #将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot #待比较数据放入最终位置
    return i #返回待比较数据最终位置

""" 快速排序"""
def quicksort(nums, left, right):
    if left < right:
        index = partition(nums, left, right)
        quicksort(nums, left, index-1)
        quicksort(nums, index+1, right)

""" topk切分
    将快速排序改成快速选择，即我们希望寻找到一个位置，这个位置左边是k个比这个位置上的数更小的数，右边是n-k个比该位置上的数大的数，将它命名为topk_split.
    找到这个位置后停止迭代，完成了一次划分。"""
def topk_split(nums, k, left, right):
    # 寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
    if (left<right):
        index = partition(nums, left, right)
        if index==k:
            return
        elif index < k:
            topk_split(nums, k, index+1, right)
        else:
            topk_split(nums, k, left, index-1)


""" 获得前k小的数"""
def topk_smalls(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    return nums[:k]

if __name__ == "__main__":
    arr = [1,3,2,3,0,-19]
    k = 2
    print("前k小的数:", topk_smalls(arr, k))
    print("topk切分后的数组:", arr, "\n")
    

""" 获得第k小的数"""
def topk_small(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    return nums[k-1] #右边是开区间，需要-1

if __name__ == "__main__":
    arr = [1,3,2,3,0,-19]
    k = 3
    print("第k小的数:", topk_small(arr, k))
    print("topk切分后的数组:", arr, "\n")


""" 获得前k大的数 """
def topk_larges(nums, k):
    #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
    topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
    return nums[len(nums)-k:]

if __name__ == "__main__":
    arr = [1,3,-2,3,0,-19]
    k = 3
    print("前k大的数:",topk_larges(arr, k))
    print("topk切分后的数组:", arr, "\n")


""" 获得第k大的数 """
def topk_large(nums, k):
    #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
    topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
    return nums[len(nums)-k]

if __name__ == '__main__':
    arr = [1,3,-2,3,0,-19]
    k = 2
    print("第k大的数:",topk_large(arr, k))
    print("topk切分后的数组:", arr, "\n")


""" 只排序前k个小的数"""
def topk_sort_left(nums, k):
    topk_split(nums, k, 0, len(nums)-1)
    topk = nums[:k]
    quicksort(topk, 0, len(topk)-1)
    return topk+nums[k:] #只排序前k个数字

if __name__ == '__main__':
    arr = [0,0,1,3,4,5,0,7,6,7]
    k = 4
    print ("只排序前k个小的的结果:", topk_sort_left(arr, k), "\n")


""" 只排序后k个大的数
    获得前n-k小的数O(n)，进行快排O(klogk) """
def topk_sort_right(nums, k):
    topk_split(nums, len(nums)-k, 0, len(nums)-1)
    topk = nums[len(nums)-k:]
    quicksort(topk, 0, len(topk)-1)
    return nums[:len(nums)-k]+topk #只排序后k个数字

if __name__ == '__main__':
    arr = [0,0,1,3,4,5,0,-7,6,7]
    k = 4
    print("只排序后k个大的数的结果:", topk_sort_right(arr, k))

