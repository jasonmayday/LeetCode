"""
https://leetcode-cn.com/problems/shortest-distance-to-a-character

给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

示例 1：
    输入：s = "loveleetcode", c = "e"
    输出：[3,2,1,0,1,0,0,1,2,2,1,0]
    解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
    距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
    距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
    对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
    距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。

示例 2：
    输入：s = "aaab", c = "b"
    输出：[3,2,1,0]

提示：
    1 <= s.length <= 10^4
    s[i] 和 c 均为小写英文字母
    题目数据保证 c 在 s 中至少出现一次

"""
from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []    # 创建 res 数组，长度为len(s)
        c_pos = [i for i in range(len(s)) if s[i] == c]   # 遍历一次字符串，并将等于 c 的下标添加至动态数组 c_pos 中。
        cur = 0     # 初始化指针cur，指向arr的 0 位置
        
        for i, x in enumerate(s):
            if cur < len(c_pos) - 1 and abs(c_pos[cur] - i) > abs(c_pos[cur + 1] - i):
                cur += 1        # 满足以上两点条件时，指针 cur 右移一位
            res.append(abs(c_pos[cur] - i))
        return res

""" 两次遍历：
    分别求每个字符到其左侧最近的字符 c 的距离，和每个字符到其左侧最近的字符 c 的距离"""
class Solution(object):
    def shortestToChar(self, S, C):
        ans = []
        prev = float('-inf')        # 初始化指针
        for i, x in enumerate(S):   # 从左向右遍历
            if x == C: prev = i     # 记录上一个字符 C 出现的位置 prev
            ans.append(i - prev)    # s[i] 到其左侧最近的字符 c 的距离就是 i - prev
        prev = float('inf')                     # 初始化指针
        for i in range(len(S) - 1, -1, -1):     # 从右向左遍历
            if S[i] == C: prev = i              # 记录上一个字符 C 出现的位置 prev，那么s[i] 到其右侧最近的字符 c 的距离就是 prev - i
            ans[i] = min(ans[i], prev - i)      # 这两个值取最小就是答案
        return ans

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_pos = [i for i in range(len(s)) if c == s[i]]     # 所有字符c出现的位置
        return([min(abs(x-i) for i in c_pos) for x in range(len(s))])

if __name__ == "__main__":
    s = "loveleetcode"
    c = "e"
    sol = Solution()
    result = sol.shortestToChar(s, c)
    print(result)
