"""
https://leetcode-cn.com/problems/three-divisors/

给你一个整数 n 。如果 n 恰好有三个正除数 ，返回 true ；否则，返回 false 。

如果存在整数 k ，满足 n = k * m ，那么整数 m 就是 n 的一个 除数 。

示例 1：
    输入：n = 2
    输出：false
    解释：2 只有两个除数：1 和 2 。

示例 2：
    输入：n = 4
    输出：true
    解释：4 有三个除数：1、2 和 4 。

提示：
    1 <= n <= 10^4

"""

"""直接模拟"""
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for x in range(1, n + 1):
            if n % x == 0:
                count += 1
                if count > 3:   # count 大于 3 时终止遍历，节省时间
                    break
        return count == 3

"""缩小范围的模拟"""
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        max_num = int(n ** 0.5)
        for x in range(1, max_num):
            if n % x == 0:
                count += 2
                if count > 3:
                    break
        if max_num ** 2 == n:
            count += 1
        return count == 3

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.isThree(n)
    print(result)