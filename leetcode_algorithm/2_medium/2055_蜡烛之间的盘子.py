"""
https://leetcode-cn.com/problems/plates-between-candles/

给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。
对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

示例 1:
    输入：s = "**|**|***|", queries = [[2,5],[5,9]]
    输出：[2,3]
    解释：
    - queries[0] 有两个盘子在蜡烛之间。
    - queries[1] 有三个盘子在蜡烛之间。

示例 2:
    输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
    输出：[9,0,0,0,0]
    解释：
    - queries[0] 有 9 个盘子在蜡烛之间。
    - 另一个查询没有盘子在蜡烛之间。

提示：
    3 <= s.length <= 10^5
    s 只包含字符 '*' 和 '|' 。
    1 <= queries.length <= 10^5
    queries[i].length == 2
    0 <= lefti <= righti < s.length

"""
from typing import List

"""方法一：预处理 + 前缀和"""
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum, sum = [0] * n, 0
        left, l = [0] * n, -1
        for i, ch in enumerate(s):
            if ch == '*':
                sum += 1
            else:
                l = i
            preSum[i] = sum
            left[i] = l

        right, r = [0] * n, -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            x, y = right[x], left[y]
            if x >= 0 and y >= 0 and x < y:
                ans[i] = preSum[y] - preSum[x]
        return ans

""" 方法一：预处理 + 前缀和"""
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        lcandle = [-1] * n      # lcandle[i] 表示在位置 i 之前(包括 i )，离 i 最近的蜡烛的位置
        rcandle = [-1] * n      # rcandle[i] 表示在位置 i 之后(包括 i )，离 i 最近的蜡烛的位置
        preSum = [0] * n        # preSum[i] 表示在位置 i 之前的盘子个数

        if s[0] == '|':         # 处理最左边情况
            lcandle[0] = 0
        if s[n - 1] == '|':     # 处理最右边情况
            rcandle[n - 1] = n - 1

        for i in range(1, n):
            lcandle[i] = i if s[i] == '|' else lcandle[i - 1]

        for i in range(n - 2, -1, -1):
            rcandle[i] = i if s[i] == '|' else rcandle[i + 1]

        for i in range(1, n):
            preSum[i] = preSum[i - 1] + 1 if s[i - 1] == '*' else preSum[i - 1]

        res = []

        for que in queries:
            left, right = que[0], que[1]

            # 首先确定查询区间内，最左侧和最右侧两个蜡烛的位置
            lidx = rcandle[left]    # left 右侧离 left 最近的蜡烛位置
            ridx = lcandle[right]   # right 左侧离 right 最近的蜡烛位置

            if lidx > right or ridx < left:
                res.append(0)
                continue

            res.append(preSum[ridx] - preSum[lidx]) # 查询区间内两个蜡烛之间的盘子个数为 prefix_plate[ridx] - prefix_plate[lidx]。

        return res

if __name__ == "__main__":
    s = "**|**|***|"
    queries = [[2,5],[5,9]]
    sol = Solution()
    result = sol.platesBetweenCandles(s, queries)
    print(result)