'''
https://leetcode-cn.com/problems/palindrome-number/

给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

示例 1：
    输入：x = 121
    输出：true

示例 2：
    输入：x = -121
    输出：false
    解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
    输入：x = 10
    输出：false
    解释：从右向左读, 为 01 。因此它不是一个回文数。

示例 4：
    输入：x = -101
    输出：false

提示：
    -2^31 <= x <= 2^31-1

'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and int(str(x)[::-1]) == x    # 如果数字大于0而且反过来等于原来数字，返回True
                                                    # a[::-1] end to beginning, counting down by 1，e.g. 210 → 012

if __name__ == "__main__":
    x = 56765
    sol = Solution()
    result = sol.isPalindrome(x)
    print (result)
