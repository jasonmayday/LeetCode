"""
https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters/

给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。

示例 1：
    输入：s = "aaabb", k = 3
    输出：3
    解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

示例 2：
    输入：s = "ababbc", k = 2
    输出：5
    解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

提示：
    1 <= s.length <= 10^4
    s 仅由小写英文字母组成
    1 <= k <= 10^5

"""
from collections import Counter

""" 递归 + 分治 """
class Solution(object):
    def longestSubstring(self, s, k):
        if not s:
            return 0
        for c in set(s):
            if s.count(c) < k:  # 如果 c 在 s 中的数量一共都不足 k 个，那么不满足条件
                return max(self.longestSubstring(t, k) for t in s.split(c))     # 只能将 s 以 c 为分隔符进行分割，对分割后的子串 t 递归调用函数
        return len(s)           # 如果 s 中所有字符 c 的数量都大于等于 k 个，则返回 s 的长度


""" 递归 """
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def recursion(s, res):
            if not s:
                return res
            count = Counter(s)
            div = ""            # 分隔字符串的字符
            for key, val in count.items():
                if val < k:     # 如果某个字符出现的次数少于 k （最小需出现的次数）
                    div = key   # 从 该字符处分割
                    break
            if not div:
                return s if len(s) > len(res) else res  # 如果整个字符串中都没有出现次数少于 k 的字符，则返回 s
            index = s.index(div)    # 分割字符的 下标
            res_left = recursion(s[:index], res)    # 被分割的左边递归
            res_right = recursion(s[index+1:], res) # 被分割的右边递归
            res = res_left if len(res_left) > len(res) else res
            res = res_right if len(res_right) > len(res) else res
            return res
        
        return len(recursion(s, ""))


if __name__ == "__main__":
    s = "ababbc"
    k = 2
    sol = Solution()
    result = sol.longestSubstring(s, k)
    print (result) 