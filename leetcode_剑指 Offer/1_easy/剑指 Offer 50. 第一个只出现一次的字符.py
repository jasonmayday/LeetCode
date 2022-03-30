"""
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
    输入：s = "abaccdeff"
    输出：'b'

示例 2:
    输入：s = ""
    输出：' '

限制：
    0 <= s 的长度 <= 50000

"""
import collections

""" 方法一：使用哈希表存储频数 """
class Solution:
    def firstUniqChar(self, s: str) -> str:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return ch
        return ' '

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic   # 若 dic 中 不包含 键(key) c ：则向 dic 中添加键值对 (c, True) ，代表字符 c 的数量为 11 ；
        for c in s:
            if dic[c]:      # 若 dic 中 包含 键(key) c ：
                return c    # 则修改键 c 的键值对为 (c, False) ，代表字符 c 的数量 > 1>1 。
        return ' '

""" 方法二：有序哈希表"""
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}    # Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():   # 遍历有序哈希表，实现搜索首个 “数量为 1 的字符”。
            if v: return k
        return ' '

if __name__ == "__main__":
    s = "abaccdeff"
    sol = Solution()
    result = sol.firstUniqChar(s)
    print(result)