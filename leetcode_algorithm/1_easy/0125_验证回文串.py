'''
https://leetcode-cn.com/problems/valid-palindrome

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:
    输入: "A man, a plan, a canal: Panama"
    输出: true
    解释："amanaplanacanalpanama" 是回文串

示例 2:
    输入: "race a car"
    输出: false
    解释："raceacar" 不是回文串
 
提示：
    1 <= s.length <= 2 * 10^5
    字符串 s 由 ASCII 字符组成

'''

"""方法1：筛选判断"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum()) # sgood: amanaplanacanalpanama
        return sgood == sgood[::-1]

"""方法2：双指针"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum()) # sgood: amanaplanacanalpanama
        n = len(sgood)
        left, right = 0, n - 1      # 初始时，左右指针分别指向 sgood 的两侧

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1       # 随后我们不断地将这两个指针相向移动，每次移动一步，并判断这两个指针指向的字符是否相同
        return True                                 # 当这两个指针相遇时，就说明 sgood 是回文串。

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    sol = Solution()
    result = sol.isPalindrome(s)
    print(result)
