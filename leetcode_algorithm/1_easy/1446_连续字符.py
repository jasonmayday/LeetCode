"""
https://leetcode-cn.com/problems/consecutive-characters/

给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
即为某个字符连续出现次数的最大值。

请你返回字符串的能量。

示例 1：
    输入：s = "leetcode"
    输出：2
    解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。

示例 2：
    输入：s = "abbcccddddeeeeedcba"
    输出：5
    解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。

示例 3：
    输入：s = "triplepillooooow"
    输出：5

示例 4：
    输入：s = "hooraaaaaaaaaaay"
    输出：11

示例 5：
    输入：s = "tourist"
    输出：1

提示：
    1 <= s.length <= 500
    s 只包含小写英文字母。

"""
class Solution:
    def maxPower(self, s: str) -> int:
        ans, count = 1, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                ans = max(ans, count)
            else:
                count = 1
        return ans

'''双指针'''
class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        left, right = 0, 1
        while right < len(s):
            if s[right] != s[left]:
                res = max(right - left, res)  # 这样写最后还要更新
                left = right
            right += 1
        return max(right - left, res)  # 必须更新

if __name__ == "__main__":
    s = "abbcccddddeeeeedcba"
    sol = Solution()
    result = sol.maxPower(s)
    print (result)