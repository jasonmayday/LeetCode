"""
https://leetcode-cn.com/problems/group-anagrams/

给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

示例 1:
    输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
    输入: strs = [""]
    输出: [[""]]

示例 3:
    输入: strs = ["a"]
    输出: [["a"]]

提示：
    1 <= strs.length <= 10^4
    0 <= strs[i].length <= 100
    strs[i] 仅包含小写字母

"""
from typing import List
from collections import defaultdict

""" 方法一：排序
    由于互为字母异位词的两个字符串包含的字母相同，因此对两个字符串分别进行排序之后得到的字符串一定是相同的，故可以将排序之后的字符串作为哈希表的键。"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))   # aet aet ant aet ant abt
            mp[key].append(st)  # key: aet; value: ['eat']
        
        return list(mp.values())

""" 方法二：计数"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    sol = Solution()
    result = sol.groupAnagrams(strs)
    print(result)