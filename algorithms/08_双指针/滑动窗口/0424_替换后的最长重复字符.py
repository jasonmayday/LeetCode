"""
https://leetcode-cn.com/problems/longest-repeating-character-replacement/

给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。

在执行上述操作后，返回包含相同字母的最长子字符串的长度。

示例 1：
    输入：s = "ABAB", k = 2
    输出：4
    解释：用两个'A'替换为两个'B',反之亦然。

示例 2：
    输入：s = "AABABBA", k = 1
    输出：4
    解释：
    将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
    子串 "BBBB" 有最长重复字母, 答案为 4。

提示：
    1 <= s.length <= 10^5
    s 仅由大写英文字母组成
    0 <= k <= s.length

"""
from collections import Counter

""" 方法1：滑动窗口
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0 for _ in range(26)]  # 记录当前窗口的字母出现次数
        left = 0    # 滑动窗口左边界
        right = 0   # 滑动窗口右边界
        res = 0     # 最长窗口长度

        while right < len(s):
            count[ord(s[right]) - ord('A')] += 1
            benchmark = max(count)              # 选择出现次数最多的字母为基准
            others = sum(count) - benchmark     # 则其他字母需要通过替换操作来变为基准
            if others <= k:                     # 通过与K进行比较来判断窗口是进行扩张？
                right += 1
                res = max(res, right-left)      # 记录当前有效窗口长度
            else:                               # 通过与K进行比较来判断窗口还是进行位移？
                count[ord(s[left])-ord('A')] -= 1
                left += 1
                right += 1                      # 这里注意：位移操作需要整个向右移，不仅仅只是left向右
        return res                              # 返回最长窗口长度

""" 方法2：滑动窗口
    另外一个表达方式：求字符串中一个最长的区间，该区间内的出现次数较少的字符的个数不超过 k。
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N = len(s)
        left, right = 0, 0  # [left, right] 都包含
        count = Counter() # 定义 count 用来统计该区间内的各个字符出现次数；
        res = 0
        while right < N:                # 第一重 while 循环是为了判断 right 指针的位置是否超出了数组边界
            count[s[right]] += 1        # 当 right 每次到了新位置，需要增加 right 指针的计数；
            while right - left + 1 - count.most_common(1)[0][1] > k:    # 第二重 while 循环让 left 指针向右移动到 [left, right] 区间符合题意的位置
                count[s[left]] -= 1     # 当 left 每次移动到了新位置，需要减少 left 指针的计数；
                left += 1
            res = max(res, right - left + 1)    # res 为 max(res, 当前区间的长度) 。
            right += 1                          # right 指针每次向右移动一步，开始探索新的区间。
        return res

if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    sol = Solution()
    result = sol.characterReplacement(s, k)
    print (result)