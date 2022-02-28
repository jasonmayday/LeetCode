"""
https://leetcode-cn.com/problems/word-break/

给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

示例 1：
    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

示例 2：
    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
         注意，你可以重复使用字典中的单词。

示例 3：
    输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    输出: false

提示：
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s 和 wordDict[i] 仅有小写英文字母组成
    wordDict 中的所有字符串 互不相同

"""
from typing import List


""" 记忆化回溯 """
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        import functools
        @functools.lru_cache(None)  # 使用记忆化函数，保存出现过的 backtrack(s)，避免重复计算。
        def back_track(s):
            if(not s):      # 若 s 长度为 0，
                return True # 则返回 True，表示已经使用 wordDict 中的单词分割完。
            res = False     # 初试化当前字符串是否可以被分割 res=Falseres=False
            for i in range(1, len(s)+1):            # 遍历结束索引 i，遍历区间 [1,n+1)：
                if(s[:i] in wordDict):              # 若 s[0,⋯,i−1] 在 wordDict 中：
                    res = back_track(s[i:]) or res  # 保存遍历结束索引中，可以使字符串切割完成的情况。
            return res
        return back_track(s)


if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    print(result)