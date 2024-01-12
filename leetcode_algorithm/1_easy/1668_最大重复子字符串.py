"""
https://leetcode-cn.com/problems/maximum-repeating-substring

给你一个字符串 sequence ，如果字符串 word 连续重复 k 次形成的字符串是 sequence 的一个子字符串，那么单词 word 的 重复值为 k 。
单词 word 的 最大重复值 是单词 word 在 sequence 中最大的重复值。如果 word 不是 sequence 的子串，那么重复值 k 为 0 。

给你一个字符串 sequence 和 word ，请你返回 最大重复值 k 。

示例 1：
    输入：sequence = "ababc", word = "ab"
    输出：2
    解释："abab" 是 "ababc" 的子字符串。

示例 2：
    输入：sequence = "ababc", word = "ba"
    输出：1
    解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。

示例 3：
    输入：sequence = "ababc", word = "ac"
    输出：0
    解释："ac" 不是 "ababc" 的子字符串。

提示：
    1 <= sequence.length <= 100
    1 <= word.length <= 100
    sequence 和 word 都只包含小写英文字母。

"""

"""二分法"""
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        left = 0
        right = len(sequence) // len(word)
        while left <= right:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1
    
"""叠加匹配字符串"""
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0   # ans 为重复次数
        s = ''  # 子字符串
        while True:
            s += word               # 从 0 个子字符串开始
            if s not in sequence:   # 如果子字符串不在sequence中
                return ans          # 返回重复值
            ans += 1                # 重复值加一，然后接着循环
            
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        for i in range(1,1000):
            if word*i not in sequence:
                return i-1

if __name__ == "__main__":
    sequence = "ababc"
    word = "ab"
    sol = Solution()
    result = sol.maxRepeating(sequence, word)
    print(result)