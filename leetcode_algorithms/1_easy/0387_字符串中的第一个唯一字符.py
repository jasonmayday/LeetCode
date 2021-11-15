"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
    s = "leetcode"
    返回 0

    s = "loveleetcode"
    返回 2
 
提示：你可以假定该字符串只包含小写字母。

"""
from collections import Counter


'''使用内置函数，二次遍历'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1


'''一次遍历，求最小值'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()
        for index, value in enumerate(s):
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1
        for index, value in enumerate(s):
            if hashmap[value] == 1:
                return index
        return -1


if __name__ == "__main__":
    s = "loveleetcode"
    sol = Solution()
    result = sol.firstUniqChar(s)
    print (result) 
