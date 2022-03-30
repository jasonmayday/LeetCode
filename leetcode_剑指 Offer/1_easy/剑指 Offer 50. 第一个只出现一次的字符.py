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

if __name__ == "__main__":
    arr = [3,2,1]
    sol = Solution()
    result = sol.getLeastNumbers(arr)
    print(result)