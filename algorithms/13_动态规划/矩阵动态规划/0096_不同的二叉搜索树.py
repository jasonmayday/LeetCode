"""
https://leetcode-cn.com/problems/unique-binary-search-trees/

给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

示例 1：
    输入：n = 3
    输出：5
    
示例 2：
    输入：n = 1
    输出：1

提示：
    1 <= n <= 19

"""

""" 动态规划
    https://pic.leetcode-cn.com/1630464953-ljIUPm-file_1630464953889"""
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)  # dp[i] 有i个连续值节点（如[1,2,3,4,5]或[5,6,7,8,9]）的不同二叉搜索树的个数
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):  # 共 i 个节点
            for left in range(i):       # 左树节点数量 0 ~ i-1 个
                right = i - 1 - left    # 右树节点数量 = 总节点数 - 根节点 - 左树节点数
                # left 个节点的BST的种类 * right 个节点的 BST 的种类
                dp[i] += dp[left] * dp[right]
        return dp[-1]   # [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670]

if __name__ == "__main__":
    n = 15
    sol = Solution()
    result = sol.numTrees(n)
    print (result)