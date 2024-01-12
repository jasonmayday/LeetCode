"""
https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/

给你一个正整数的数组 A。

然后计算 S，使其等于数组 A 当中最小的那个元素各个数位上数字之和。

最后，假如 S 所得计算结果是 奇数 ，返回 0 ；否则请返回 1。

示例 1:
    输入：[34,23,1,24,75,33,54,8]
    输出：0
    解释：
        最小元素为 1 ，该元素各个数位上的数字之和 S = 1 ，是奇数所以答案为 0 。

示例 2：
    输入：[99,77,33,66,55]
    输出：1
    解释：
        最小元素为 33 ，该元素各个数位上的数字之和 S = 3 + 3 = 6 ，是偶数所以答案为 1 。

提示：
    1 <= A.length <= 100
    1 <= A[i] <= 100

"""

from typing import List

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        x = min(A)
        res = 0
        while x:
            res += (x % 10)
            x //= 10
        return 0 if res % 2 == 1 else 1

if __name__ == "__main__":
    A = [34,23,1,24,75,33,54,8]
    sol = Solution()
    result = sol.sumOfDigits(A)
    print(result)