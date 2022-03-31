"""
https://leetcode-cn.com/problems/qIsx9U/

给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

实现 MovingAverage 类：
    MovingAverage(int size) 用窗口大小 size 初始化对象。
    double next(int val) 计算并返回数据流中最后 size 个值的移动平均值。

示例：
    输入：
        ["MovingAverage", "next", "next", "next", "next"]
        [[3], [1], [10], [3], [5]]
    输出：
        [null, 1.0, 5.5, 4.66667, 6.0]

    解释：
        MovingAverage movingAverage = new MovingAverage(3);
        movingAverage.next(1); // 返回 1.0 = 1 / 1
        movingAverage.next(10); // 返回 5.5 = (1 + 10) / 2
        movingAverage.next(3); // 返回 4.66667 = (1 + 10 + 3) / 3
        movingAverage.next(5); // 返回 6.0 = (10 + 3 + 5) / 3

提示：
    1 <= size <= 1000
    -10^5 <= val <= 10^5
    最多调用 next 方法 10^4 次

"""
from collections import deque

""" 方法一：数组或列表 """
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = []   # 初始化 queue 来存储数据流的数据和移动窗口 n 的大小。

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)               # 首先将 val 添加到 queue 中
        window_sum = sum(queue[-size:]) # 从 queue 取最后 n 个元素计算平均值。
        return window_sum / min(len(queue), size)


""" 方法二：双端队列 """
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0      # number of elements seen so far

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.size, self.count)

if __name__ == "__main__":
    movingAverage = MovingAverage(3)
    print(movingAverage.next(1))   # 返回 1.0 = 1 / 1
    print(movingAverage.next(10))  # 返回 5.5 = (1 + 10) / 2
    print(movingAverage.next(3))   # 返回 4.66667 = (1 + 10 + 3) / 3
    print(movingAverage.next(5))   # 返回 6.0 = (10 + 3 + 5) / 3