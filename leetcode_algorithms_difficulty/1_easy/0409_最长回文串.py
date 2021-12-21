"""
https://leetcode-cn.com/problems/longest-palindrome/

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

注意:
    假设字符串的长度不会超过 1010。

示例 1:
    输入:
    "abccccdd"

    输出:
    7

    解释:
    我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s).values()     # 统计各字符次数，eg:"ddsad":[3, 1, 1]
        x = sum([item//2*2 for item in count if (item//2 > 0)])     # 统计两两配对的字符总个数，eg: {"ddass":4,"ddsss":4}
        if x == len(s):         # 判断是否有没配对的单字符，
            return x            # 没有的话返回 x, eg: {"ddss": 4}
        else:                   # 有的话结果加 1。 
            return x + 1        # eg: {"ddss":4, "ddhjSS":4+1}-->{"ddss":4, "ddhjSS":5}

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)          # 统计字符词频
        center = 0
        res = 0
        for char in count:              # 判断各个字符的词频奇偶
            if count[char] % 2:         # 对于所有的出现奇数次的字符，那么实际上我们就可以看作是 1+偶数次
                center = 1              # center置为1
                res += count[char] - 1  # 比如一个字符出现5次，只有4个可用，2个各放在两边，1个放在正中间
            else:                       # 对于所有的出现偶数次的字符，那么其实在组回文字符串的时候就是可以看作直接放置在中心两侧
                res += count[char]      # 因此有多少就直接加上去多少就好了
        return res + center

if __name__ == "__main__":
    s = "ddsad"
    sol = Solution()
    result = sol.longestPalindrome(s)
    print(result)