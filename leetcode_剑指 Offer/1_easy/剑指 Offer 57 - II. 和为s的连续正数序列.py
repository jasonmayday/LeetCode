"""
https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/

输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
    输入：target = 9
    输出：[[2,3,4],[4,5]]

示例 2：
    输入：target = 15
    输出：[[1,2,3,4,5],[4,5,6],[7,8]]

限制：
    1 <= target <= 10^5

"""
from typing import List

""" 方法一：求和公式"""
class Solution:
    def findContinuousSequence(self, target: int):
        i, j = 1, 2
        res = []
        while i < j:
            j = (-1 + (1 + 4 * (2 * target + i * i - i)) ** 0.5) / 2
            if i < j and j == int(j):
                res.append(list(range(i, int(j) + 1)))
            i += 1
        return res

""" 方法二：滑动窗口（双指针）"""
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j = 1, 2
        s = 3   # 元素和
        res = []
        while i < j:    # 当 i≥j 时跳出
            if s == target:                         # 当元素和等于目标时
                res.append(list(range(i, j + 1)))   # 记录连续整数序列
            if s > target:  # 当元素和大于目标时
                s -= i      # 更新元素和 s，向右移动左边界 i=i+1
                i += 1      # i 向右移，代表元素 i 被移除了窗口，因此要先 减去值，再右移左指针
            else:           # 当元素和小于目标时
                j += 1      # 向右移动右边界 j=j+1，更新元素和 s
                s += j      # 右边情况不一样，先右移才能把元素包含进来
        return res

if __name__ == "__main__":
    target = 9
    sol = Solution()
    result = sol.findContinuousSequence(target)
    print(result)