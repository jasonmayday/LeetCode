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


""" 动态规划 """
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:       
        n = len(s)
        dp = [False] * (n+1)    # dp[i] 表示 s 的前 i 位是否可以用 wordDict 中的单词表示。[False, False, False, False, False, False, False, False, False, False]
        dp[0] = True            # 前 0 位(空字符)可以被表示。[True, False, False, False, False, False, False, False, False, False]
        for i in range(n):
            for j in range(i+1, n+1):
                if(dp[i] == True and (s[i:j] in wordDict)): # 若 dp[i]=True 说明 s 的前 i 位可以用 wordDict 表示，且 s[i,⋯,j) 出现在 wordDict 中
                    dp[j] = True                            # 说明 s 的前 j 位也可以表示。
        return dp[-1]


if __name__ == "__main__":
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)
    print(result)