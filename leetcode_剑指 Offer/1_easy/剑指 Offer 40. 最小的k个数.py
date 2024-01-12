"""
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
    输入：arr = [3,2,1], k = 2
    输出：[1,2] 或者 [2,1]

示例 2：
    输入：arr = [0,1,2,1], k = 1
    输出：[0]

限制：
    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000

"""
import random
import heapq
from typing import List

""" 方法1：排序"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        return arr[:k]


""" 方法2：堆"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
                                    # Python 语言中的堆为小根堆，因此我们要对数组中所有的数取其相反数
        hp = [-x for x in arr[:k]]  # 首先将前 k 个数插入大根堆中
        heapq.heapify(hp)           # 用一个大根堆实时维护数组的前 k 小值
        for i in range(k, len(arr)):    # 从第 k+1 个数开始遍历
            if -hp[0] > arr[i]:         # 如果当前遍历到的数比大根堆的堆顶的数要小
                heapq.heappop(hp)           # 就把堆顶的数弹出
                heapq.heappush(hp, -arr[i]) # 再插入当前遍历到的数
        ans = [-x for x in hp]      # 最后将大根堆里的数存入数组返回即可。
        return ans


""" 方法3：手动快速排序"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def quick_sort(arr, l, r):
            if l >= r: return   # 子数组长度为 1 时终止递归
            i, j = l, r     # 初始化哨兵索引位置（以 arr[l] 作为基准数）
            while i < j:    # 循环交换，两哨兵相遇时跳出
                while i < j and arr[j] >= arr[l]:   # 从右向左，查抄首个小于基准数的元素
                    j -= 1
                while i < j and arr[i] <= arr[l]:   # 从左向右，查抄首个大于基准数的元素
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]     # 交换arr[i] 和 arr[j]
            arr[l], arr[i] = arr[i], arr[l]     # 交换基准数 arr[l] 和 arr[i]
            # 哨兵划分操作完成后，左子数组所有数字 ≤ 基准数，右子数组所有数字 ≥ 基准数
            quick_sort(arr, l, i - 1)   # 递归左（右）子数组执行哨兵划分
            quick_sort(arr, i + 1, r)
        
        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]


""" 方法4：基于快速排序的数组划分
    题目只要求返回最小的 k 个数，对这 k 个数的顺序并没有要求。因此，只需要将数组划分为 最小的 k 个数 和 其他数字 两部分即可，而快速排序的哨兵划分可完成此目标。
    根据快速排序原理，如果某次哨兵划分后 基准数正好是第 k+1 小的数字 ，那么此时基准数左边的所有数字便是题目所求的 最小的 k 个数 。"""
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr):   # 若 k 大于数组长度，则直接返回整个数组；
            return arr
        def quick_sort_smallest_k(l, r):    # 函数搜索并返回最小的 kk 个数
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i:                                   # 若 k<i ，代表第 k+1 小的数字在 左子数组 中
                return quick_sort_smallest_k(l, i - 1)  # 递归左子数组
            if k > i:                                   # 若 k>i ，代表第 k+1 小的数字在 右子数组 中
                return quick_sort_smallest_k(i + 1, r)  # 递归右子数组
            return arr[:k]  # 若 k=i ，代表此时 arr[k] 即为第 k+1 小的数字，则直接返回数组前 k 个数字即可；
            
        return quick_sort_smallest_k(0, len(arr) - 1)


""" 方法5：快排思想
    快排的划分函数每次执行完后都能将数组分成两个部分，小于等于分界值 pivot 的元素的都会被放到数组的左边，大于的都会被放到数组的右边，然后返回分界值的下标。
    与快速排序不同的是，快速排序会根据分界值的下标递归处理划分的两侧，而这里我们只处理划分的一边。"""
class Solution:
    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[r] = nums[r], nums[i + 1]
        return i + 1

    def randomized_partition(self, nums, l, r):
        i = random.randint(l, r)
        nums[r], nums[i] = nums[i], nums[r]
        return self.partition(nums, l, r)

    def randomized_selected(self, arr, l, r, k):    # 函数划分数组 arr 的 [l,r] 部分，使前 k 小的数在数组的左侧
        pos = self.randomized_partition(arr, l, r)  # 调用快排的划分函数，返回的下标是 pos（表示分界值 pivot 最终在数组中的位置）
        num = pos - l + 1   # num是数组中第 pos - l + 1 小的数
        if k < num:         # 表示第 k 小的数在 num 的左侧
            self.randomized_selected(arr, l, pos - 1, k)        # 左侧递归
        elif k > num:       # 表示第 k 小的数在 num 的右侧
            self.randomized_selected(arr, pos + 1, r, k - num)  # 右侧递归

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return list()
        self.randomized_selected(arr, 0, len(arr) - 1, k)
        return arr[:k]

if __name__ == "__main__":
    arr = [3,2,1]
    sol = Solution()
    result = sol.getLeastNumbers(arr)
    print(result)