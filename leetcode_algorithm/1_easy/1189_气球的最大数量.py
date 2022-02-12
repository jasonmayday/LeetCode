"""
https://leetcode-cn.com/problems/maximum-number-of-balloons/

给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

示例 1：
    输入：text = "nlaebolko"
    输出：1

示例 2：
    输入：text = "loonbalxballpoon"
    输出：2

示例 3：
    输入：text = "leetcode"
    输出：0

提示：
    1 <= text.length <= 10^4
    text 全部由小写英文字母组成

"""
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)   # {'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2, 'x': 1, 'p': 1}
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])
    
    
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(ch for ch in text if ch in "balon")   # 只统计需要的字母
        cnt['l'] //= 2  # "balloon" 中有两个'l'和'o'
        cnt['o'] //= 2
        if len(cnt) == 5:
            return min(cnt.values()) 
        else: return 0


if __name__ == "__main__":
    text = "loonbalxballpoon"
    sol = Solution()
    result = sol.maxNumberOfBalloons(text)
    print(result)