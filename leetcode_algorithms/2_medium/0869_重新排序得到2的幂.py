'''
https://leetcode-cn.com/problems/reordered-power-of-2/

给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

示例 1：
输入：1
输出：true

示例 2：
输入：10
输出：false

示例 3：
输入：16
输出：true

示例 4：
输入：24
输出：false

示例 5：
输入：46
输出：true

提示：
1 <= N <= 10 ^ 9

'''



import collections

class Solution:
    def reorderedPowerOf2(self, n):
        count = collections.Counter(str(n))   # 原本数字n的计数，Counter({'4': 1, '6': 1})
        for i in range(31):                   # 因为 10 ^ 9 < 2 ^ 30， 所以2的次方数，也就2^0,2^1,2^2.......2^30，共31个
            if count == collections.Counter(str(1 << i)):
                return True
        return False
if __name__ == "__main__":
    n = 46
    sol = Solution()
    result = sol.reorderedPowerOf2(n)
    print(result)