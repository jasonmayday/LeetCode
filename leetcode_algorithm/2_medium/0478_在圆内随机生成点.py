"""
https://leetcode.cn/problems/generate-random-point-in-a-circle/

给定圆的半径和圆心的位置，实现函数 randPoint ，在圆中产生均匀随机点。

实现 Solution 类:
    Solution(double radius, double x_center, double y_center) 用圆的半径 radius 和圆心的位置 (x_center, y_center) 初始化对象
    randPoint() 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 [x, y] 。

示例 1：
    输入:
    ["Solution","randPoint","randPoint","randPoint"]
    [[1.0, 0.0, 0.0], [], [], []]
    输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
    解释:
    Solution solution = new Solution(1.0, 0.0, 0.0);
    solution.randPoint ();//返回[-0.02493，-0.38077]
    solution.randPoint ();//返回[0.82314,0.38945]
    solution.randPoint ();//返回[0.36572,0.17248]

提示：
    0 < radius <= 10^8
    -10^7 <= x_center, y_center <= 10^7
    randPoint 最多被调用 3 * 10^4 次

"""
import random
import math
from math import sqrt
from typing import List

""" 方法一：拒绝采样
    使用一个边长为 2R 的正方形覆盖住圆，并在正方形内生成均匀随机点，
    拒绝掉那些不在题目给定范围内的随机数，此时保留下来的随机数都是在范围内的。"""
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        while True:
            x, y = random.uniform(-self.r, self.r), random.uniform(-self.r, self.r)
            if x * x + y * y <= self.r * self.r:
                return [self.xc + x, self.yc + y]

"""方法二：计算分布函数"""
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.xc = x_center
        self.yc = y_center
        self.r = radius

    def randPoint(self) -> List[float]:
        u, theta = random.random(), random.random() * 2 * math.pi
        r = sqrt(u)
        return [self.xc + r * math.cos(theta) * self.r, self.yc + r * math.sin(theta) * self.r]

if __name__ == "__main__":
    solution = Solution(1.0, 0.0, 0.0)
    print (solution.randPoint ())
    print (solution.randPoint ())
    print (solution.randPoint ())