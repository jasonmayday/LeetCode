"""
https://leetcode-cn.com/problems/container-with-most-water/

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

示例 1：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49 
    解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

示例 2：
    输入：height = [1,1]
    输出：1

示例 3：
    输入：height = [4,3,2,1,4]
    输出：16

示例 4：
    输入：height = [1,2,1]
    输出：2

提示：
    n == height.length
    2 <= n <= 10^5
    0 <= height[i] <= 10^4

"""
from typing import List

""" 双指针
    面积公式 ：S(i,j) = min(h[i], h[j]) × (j - i) """
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0                   # 左指针（最左）
        j = len(height) - 1     # 右指针（最右）
        res = 0
        while i < j:            # 移动指针，总体思想为移动短的板子，因为若移动长板，面积一定变小
            if height[i] < height[j]:                   # 左边低
                res = max(res, height[i] * (j - i))     # 面积 = 低的高度 × 水槽板距离
                i += 1  
            else:                                       # 右边低
                res = max(res, height[j] * (j - i))
                j -= 1
        return res

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    result = sol.maxArea(height)
    print (result)