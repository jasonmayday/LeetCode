"""
https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

给你一个字符串 s ，如果 s 是一个 好 字符串，请你返回 true ，否则请返回 false 。

如果 s 中出现过的 所有 字符的出现次数 相同 ，那么我们称字符串 s 是 好 字符串。

示例 1：
    输入：s = "abacbc"
    输出：true
    解释：s 中出现过的字符为 'a'，'b' 和 'c' 。s 中所有字符均出现 2 次。

示例 2：
    输入：s = "aaabb"
    输出：false
    解释：s 中出现过的字符为 'a' 和 'b' 。
    'a' 出现了 3 次，'b' 出现了 2 次，两者出现次数不同。

提示：
    1 <= s.length <= 1000
    s 只包含小写英文字母。

"""
from collections import Counter

"""使用Counter"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        return len(set(Counter(s).values())) == 1   # {'a': 2, 'b': 2, 'c': 2}

"""字典解法 比较最大最小value值的key"""
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}
        for i in s:
            dic[i] = s.count(i)
        if min(dic,key = dic.get) == max(dic,key=dic.get):
            return True
        else:
            return False

if __name__ == "__main__":
    s = "abacbc"
    sol = Solution()
    result = sol.areOccurrencesEqual(s)
    print(result)