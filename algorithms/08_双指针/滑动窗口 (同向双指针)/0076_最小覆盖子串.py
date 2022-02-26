"""
https://leetcode-cn.com/problems/minimum-window-substring/

给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：
    对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
    如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：
    输入：s = "ADOBECODEBANC", t = "ABC"
    输出："BANC"

示例 2：
    输入：s = "a", t = "a"
    输出："a"

示例 3:
    输入: s = "a", t = "aa"
    输出: ""
    解释: t 中两个字符 'a' 均应包含在 s 的子串中，
    因此没有符合条件的子字符串，返回空字符串。

提示：
    1 <= s.length, t.length <= 10^5
    s 和 t 由英文字母组成

进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？

"""
from collections import defaultdict

""" 滑动窗口 """
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for ch in t:        # 统计需要的字符的个数
            need[ch] += 1   # {'A': 1, 'B': 1, 'C': 1}
        needCnt = len(t)
        i = 0
        res = (0, float('inf'))
        for j, c in enumerate(s):   # 遍历所有字符
            if need[c] > 0:         # 需要字符c
                needCnt -= 1        # 还需要的字符数减一
            need[c] -= 1            # 把右边的字符加入窗口
            if needCnt == 0:        # 如果还需要的字符数 减到0，说明滑动窗口包含了所有 t 元素
                while True:         
                    c = s[i] 
                    if need[c] == 0:
                        break
                    need[c] += 1    
                    i += 1          # 右移 i，排除多余元素
                if j - i < res[1] - res[0]:   # 记录结果
                    res = (i, j)
                need[s[i]] += 1     # 向右移动后窗口肯定不能满足了 重新开始循环i 增加一个位置，寻找新的满足条件滑动窗口
                needCnt += 1
                i += 1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]    # 如果res始终没被更新过，代表无满足条件的结果


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    result = sol.minWindow(s, t)
    print(result)