"""
https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

示例 1:
    输入: s = "cbaebabacd", p = "abc"
    输出: [0,6]
    解释:
    起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
    起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

示例 2:
    输入: s = "abab", p = "ab"
    输出: [0,1,2]
    解释:
    起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
    起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
    起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

提示:
    1 <= s.length, p.length <= 3 * 10^4
    s 和 p 仅包含小写字母

"""
from typing import List

''' 滑动窗口 '''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Step 1:
        # 定义需要维护的变量
        # 本文需要对比两组字符串是否为异位词，所以用哈希表 (abc和bac是异位词是因为他们对应的哈希表相等)
        # 同时我们需要找到所有合法解，所以还需要一个res数组
        res, hashmap = [], {}

        # Step 1.1： 同时把p的哈希表也建立了 (这个哈希表不需要维护，为定值)
        hashmap_p = {}
        for char in p:
            hashmap_p[char] = hashmap_p.get(char, 0) + 1

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量 (hashmap)， 如果hashmap == hashmap_p，代表找到了一个解，加入到res
            hashmap[s[end]] = hashmap.get(s[end], 0) + 1
            if hashmap == hashmap_p:
                res.append(start)

            # Step 4
            # 根据题意可知窗口长度固定，所以用if
            # 窗口左指针前移一个单位保证窗口长度固定, 同时提前更新需要维护的变量 (hashmap)
            if end >= len(p) - 1:
                hashmap[s[start]] -= 1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start += 1
        # Step 5: 返回答案
        return res

''' 滑动窗口 '''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len, p_len = len(s), len(p)
        ans = []
        if s_len < p_len:
            return []       # 当字符串 s 的长度小于字符串 p 的长度时，字符串 s 中一定不存在字符串 p 的异位词。

        s_count = [0] * 26  # 因为字符串中的字符全是小写字母，可以用长度为26的数组记录字母出现的次数
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:
            ans.append(0)

        for i in range(s_len - p_len):
            s_count[ord(s[i]) - 97] -= 1
            s_count[ord(s[i + p_len]) - 97] += 1

            if s_count == p_count:
                ans.append(i + 1)

        return ans

if __name__ == "__main__":
    s = "abab"
    p = "ab"
    sol = Solution()
    result = sol.findAnagrams(s,p)
    print (result)