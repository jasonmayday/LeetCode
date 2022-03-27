"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。

给你一个可能存在 重复 元素值的数组 numbers ，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。请返回旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。  

注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

示例 1：
    输入：numbers = [3,4,5,1,2]
    输出：1

示例 2：
    输入：numbers = [2,2,2,0,1]
    输出：0

提示：
    n == numbers.length
    1 <= n <= 5000
    -5000 <= numbers[i] <= 5000
    numbers 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""
from typing import List

""" 方法一：二分查找
    数组中的最后一个元素 x：
    在最小值右侧的元素，它们的值一定都小于等于 x；
    而在最小值左侧的元素，它们的值一定都大于等于 x。
    因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。
"""
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        left = 0
        right = len(numbers) - 1
        while left < right:
            mid = left + (right - left) // 2     # mid 为区间的中点
            if numbers[mid] < numbers[right]:
                right = mid                      # 说明 numbers[mid] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分。
            elif numbers[mid] > numbers[right]:
                left = mid + 1                   # 说明 numbers[mid] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分。
            else:               # 第三种情况是 numbers[mid] == numbers[high]
                right -= 1      # 由于重复元素的存在，我们并不能确定 numbers[mid] 究竟在最小值的左侧还是右侧，可以忽略二分查找区间的右端点
        return numbers[left]

if __name__ == "__main__":
    numbers = [3,4,5,1,2]
    sol = Solution()
    result = sol.minArray(numbers)
    print(result)
