"""
https://leetcode-cn.com/problems/lexicographical-numbers/

给你一个整数 n ，按字典序返回范围 [1, n] 内所有整数。

你必须设计一个时间复杂度为 O(n) 且使用 O(1) 额外空间的算法。

示例 1：
    输入：n = 13
    输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]

示例 2：
    输入：n = 2
    输出：[1,2]

提示：
    1 <= n <= 5 * 10^4

"""
from typing import List

""" 方法一：深度优先搜索
    [1,n] 范围内的所有整数的字典序实际上就是字典树的先序遍历顺序。"""
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(num):
            if num > n: # 递归终点
                return
            ans.append(num)
            for i in range(10):
                dfs(num * 10 + i)
        
        ans = []
        for num in range(1, 10):
            dfs(num)
        return ans
    
""" 方法二：迭代 """
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        num = 1
        while len(ans) < n:
            while num <= n:     # 不断进入下一层
                ans.append(num)
                num *= 10
            while num % 10 == 9 or num > n:  # 不断返回上一层
                num //= 10
            num += 1            # 遍历该层下一个数
        return ans

if __name__ == "__main__":
    n = 13
    sol = Solution()
    result = sol.lexicalOrder(n)
    print (result)