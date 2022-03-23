"""
https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/

给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

示例 1:
    输入: n = 13, k = 2
    输出: 10
    解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

示例 2:
    输入: n = 1, k = 1
    输出: 1

提示:
    1 <= k <= n <= 10^9

"""

""" 字典树
    前序遍历该字典树即可得到字典序从小到大的数字序列，遍历到第 k 个节点即为第 k 小的数字。"""
class Solution:
    def getSteps(self, cur: int, n: int) -> int:
        steps = 0
        first = cur
        last = cur
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        cur = 1
        k -= 1
        while k:
            steps = self.getSteps(cur, n)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                cur *= 10
                k -= 1
        return cur

if __name__ == "__main__":
    n = 13
    k = 2
    sol = Solution()
    result = sol.findKthNumber(n, k)
    print(result)