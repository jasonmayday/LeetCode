"""
https://leetcode-cn.com/problems/add-to-array-form-of-integer/

对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

示例 1：
    输入：A = [1,2,0,0], K = 34
    输出：[1,2,3,4]
    解释：1200 + 34 = 1234

示例 2：
    输入：A = [2,7,4], K = 181
    输出：[4,5,5]
    解释：274 + 181 = 455

示例 3：
    输入：A = [2,1,5], K = 806
    输出：[1,0,2,1]
    解释：215 + 806 = 1021

示例 4：
    输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
    输出：[1,0,0,0,0,0,0,0,0,0,0]
    解释：9999999999 + 1 = 10000000000

提示：
    1 <= A.length <= 10000
    0 <= A[i] <= 9
    0 <= K <= 10000
    如果 A.length > 1，那么 A[0] != 0

"""
from typing import List

class Solution(object):
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        res = []    # 维护一个答案数组
        i = len(A) - 1
        carry = 0
        while i >= 0 or K != 0:
            x = A[i] if i >= 0 else 0
            y = K % 10 if K != 0 else 0

            sum = x + y + carry
            res.append(sum % 10)
            carry = sum // 10

            i -= 1
            K //= 10
        if carry != 0: res.append(carry)
        return res[::-1]

class Solution(object):
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        


if __name__ == "__main__":
    A = [9,9,9,9,9,9,9,9,9,9]
    K = 1
    sol = Solution()
    result = sol.addToArrayForm(A, K)
    print (result)