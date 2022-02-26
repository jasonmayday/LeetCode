'''
堆排序(Heap Sort)是利用堆这种数据结构而设计的一种排序算法，是一种选择排序。
堆是具有以下性质的完全二叉树：
    每个结点的值都大于或等于其左右孩子结点的值，称为大顶堆；
    或者每个结点的值都小于或等于其左右孩子结点的值，称为小顶堆。

堆排序思路为: 将一个无序序列调整为一个堆，就能找出序列中的最大值（或最小值），
然后将找出的这个元素与末尾元素交换，这样有序序列元素就增加一个，无序序列元素就减少一个，
对新的无序序列重复操作，从而实现排序。

算法实现步骤
    构造初始堆。将给定无序序列构造成一个大顶堆（一般升序采用大顶堆，降序采用小顶堆)；
    将堆顶元素与末尾元素进行交换，使末尾元素最大。然后继续调整堆，再将堆顶元素与末尾元素交换，得到第二大元素；
    重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素；
    如此反复进行交换、重建、交换，直到整个序列有序。
'''

from typing import List

def build(arr:List[int], root, end):
    while True:
        child = 2 * root + 1 # 左子节点的位置
        if child > end:      # 若左子节点超过了最后一个节点，则终止循环
            break
        if (child + 1 <= end) and (arr[child + 1] > arr[child]): # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
            child += 1
        if arr[child] > arr[root]: # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break

def heap_sort(arr:List[int]):
    n = len(arr)
    first_root = n // 2 - 1 # 确认最深最后的那个根节点的位置
    for root in range(first_root, -1, -1): # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr, root, n - 1)
        
    for end in range(n - 1, 0, -1): # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
        arr[0], arr[end] = arr[end], arr[0]
        build(arr, 0, end - 1)


if __name__ == '__main__':
    import random
    random.seed(10)
    arr = [random.randint(0,100) for _ in range(20)]
    print("原始数据：", arr)
    heap_sort(arr)
    print("堆排序：", arr)