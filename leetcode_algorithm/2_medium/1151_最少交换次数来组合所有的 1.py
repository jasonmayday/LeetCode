"""
https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together/

给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。

示例 1:
    输入: data = [1,0,1,0,1]
    输出: 1
    解释:
        有三种可能的方法可以把所有的 1 组合在一起：
        [1,1,1,0,0]，交换 1 次；
        [0,1,1,1,0]，交换 2 次；
        [0,0,1,1,1]，交换 1 次。
        所以最少的交换次数为 1。

示例 2:
    输入: data = [0,0,0,1,0]
    输出: 0
    解释:
        由于数组中只有一个 1，所以不需要交换。

示例 3:
    输入: data = [1,0,1,0,1,0,0,1,1,0,1]
    输出: 3
    解释:
        交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。

示例 4:
    输入: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
    输出: 8

提示:
    1 <= data.length <= 10^5
    data[i] == 0 or 1.

"""
from typing import List

""" 滑动窗口 """
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        window_len = sum(data)          # 数组中所有1的个数，作为滑动窗口的长度
        cnt1 = sum(data[ :window_len])  # 初始化滑动窗口，第一个窗口内1的个数
        res = window_len - cnt1         # 第一个窗口内0的个数（也就是初始化的答案：需要交换的次数）

        for i in range(window_len, n):  # 滑动窗口
            cnt1 += data[i]             # 进R
            cnt1 -= data[i - window_len]# 弹L
            cnt0 = window_len - cnt1    # 窗口内0的个数 = 如果以此窗口的位置为最后结果，需要交换的次数
            res = min(res, cnt0)        # 更新 res
        return res

if __name__ == "__main__":
    data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
    sol = Solution()
    result = sol.minSwaps(data)
    print(result)