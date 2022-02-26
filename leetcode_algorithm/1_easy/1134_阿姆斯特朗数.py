"""
https://leetcode-cn.com/problems/armstrong-number/

给你一个整数 n ，让你来判定他是否是 阿姆斯特朗数，是则返回 true，不是则返回 false。

假设存在一个 k 位数 n ，其每一位上的数字的 k 次幂的总和也是 n ，那么这个数是阿姆斯特朗数 。

示例 1：
    输入：n = 153
    输出：true
    示例：
        153 是一个 3 位数，且 153 = 1^3 + 5^3 + 3^3。

示例 2：
    输入：n = 123
    输出：false
    解释：123 是一个 3 位数，且 123 != 1^3 + 2^3 + 3^3 = 36。

提示：
    1 <= n <= 10^8

"""

class Solution(object):
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        sum = 0
        for i in str(n):
            sum += int(i) ** k
        return sum == n

class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum(map(lambda c: int(c) ** len(str(n)), str(n))) == n

if __name__ == "__main__":
    n = 153
    sol = Solution()
    result = sol.isArmstrong(n)
    print(result)

