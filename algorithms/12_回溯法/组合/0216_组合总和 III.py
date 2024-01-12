"""
https://leetcode-cn.com/problems/combination-sum-iii/

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

在 [1,2,3,4,5,6,7,8,9] 这个集合中找到和为 n 的 k 个数的组合。

说明：
    所有数字都是正整数。
    解集不能包含重复的组合。 

示例 1:
    输入: k = 3, n = 7
    输出: [[1,2,4]]

示例 2:
    输入: k = 3, n = 9
    输出: [[1,2,6], [1,3,5], [2,3,4]]

"""
from typing import List

""" 回溯法
    树的深度 = k
    树的宽度 = 9（因为整个集合就是9个数）"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []    # 存放结果集
        path = []   # 符合条件的结果
        def findallPath(n, k, sum, startIndex):
            if sum > n:     # 已选元素总和如果已经大于 n 了，
                return      # 那么往后遍历就没有意义了，直接剪掉。
            if sum == n and len(path) == k:  # 如果path.size() == k 但sum != n 直接返回
                return res.append(path[:])
            for i in range(startIndex, 9-(k-len(path))+2):  # 剪枝操作，(for循环，横向遍历)(从左向右取数，取过的数不再重复取)
                path.append(i)  # 处理
                sum += i        # 处理
                findallPath(n,k,sum,i+1)  # 注意i+1调整startIndex，(递归，纵向遍历)
                sum -= i    # 回溯
                path.pop()  # 回溯
        
        findallPath(n,k,0,1)
        return res

if __name__ == "__main__":
    k = 3
    n = 9
    sol = Solution()
    result = sol.combinationSum3(k, n)
    print (result)