"""
https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string/

给你一个由若干 0 和 1 组成的字符串 s ，请你计算并返回将该字符串分割成两个 非空 子字符串（即 左 子字符串和 右 子字符串）所能获得的最大得分。

「分割字符串的得分」为 左 子字符串中 0 的数量加上 右 子字符串中 1 的数量。

示例 1：
    输入：s = "011101"
    输出：5 
    解释：
    将字符串 s 划分为两个非空子字符串的可行方案有：
    左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5 
    左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4 
    左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3 
    左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2 
    左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3

示例 2：
    输入：s = "00111"
    输出：5
    解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5

示例 3：
    输入：s = "1111"
    输出：3

提示：
    2 <= s.length <= 500
    字符串 s 仅由字符 '0' 和 '1' 组成。

"""

"""解法1"""
class Solution:
    def maxScore(self, s: str) -> int:
        max = 0
        for i in range(1, len(s)):
            left = s[:i].count('0')
            right = s[i:].count('1')
            if ((left + right) > max):
                max = left + right
        return max

"""解法2"""
class Solution:
    def maxScore(self, s: str) -> int:
        sum = s.count('1')  # 先行遍历，得到整个字符串的1的个数
        ans = 0
        for i in s[:-1]:        # 字符串遍历，记录每种划分的和，取最大值。[:-1]指除去最后一个元素，否则与题意【分割成两个非空子字符串】矛盾
            if i == '1':        # 对于每种划分，左边
                sum = sum - 1
            if i == '0':
                sum = sum + 1
            ans = max(ans, sum)
        return ans
    
"""解法3：直接分隔"""
class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:i].count("0") + s[i:].count("1") for i in range(1, len(s)))
    
"""解法4：动态维护左边的 0 的总数和右侧 1 的总数"""
class Solution:
    def maxScore(self, s: str) -> int:
        right = s.count('1')  # 代表右侧的 1 的个数
        left = 0  # 代表左侧的 0 的个数
        score = 0
        for idx in range(len(s) - 1):
            if s[idx] == '1':
                score = max(score, (left + right - 1))
                right -= 1
            else:
                score = max(score, (left + 1 + right))
                left += 1
        return score

if __name__ == "__main__":
    s = "011101"
    sol = Solution()
    result = sol.maxScore(s)
    print(result)