"""
https://leetcode-cn.com/problems/parallel-courses-ii/

给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。

在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

示例 1：
    输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
    输出：3 
    解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。

示例 2：
    输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
    输出：4 
    解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。

示例 3：
    输入：n = 11, dependencies = [], k = 2
    输出：6

提示：
    1 <= n <= 15
    1 <= k <= n
    0 <= dependencies.length <= n * (n-1) / 2
    dependencies[i].length == 2
    1 <= xi, yi <= n
    xi != yi
    所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
    题目输入的图是个有向无环图。

"""

from typing import List
from collections import defaultdict
from math import ceil

""" 状态压缩 动态规划 """
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        if len(relations) == 0:
            return ceil(n / k)  # ceil() 返回数字的上入整数。
        if len(relations) == 1:
            res = ceil(n / k)
            return 2 if res == 1 else res

        # 计算修读集合s的课程之后能够再修的所有的课程组成的集合
        def get_nex_all(s):
            s_nex_all = 0
            for c in range(n):
                # 如果c的前序课程为s的子集, 且c不在s集合中，则纳入课程c
                if dic_pre[c]&s == dic_pre[c] and 1 << c & s == 0:
                    s_nex_all|=1<<c
            return s_nex_all

        # 获得s_nex_all的所有的非空子集的压缩码
        def get_subset(s_nex_all):
            s_tempt = s_nex_all
            res=set()
            while s_tempt:
                if s_tempt != 0: res.add(s_tempt)
                s_tempt = (s_tempt-1) & s_nex_all #很重要 如果一个个数就要超时啦
            return res

        # 先把课程1～n转换成0～n-1和数组的inde相对应上
        relations = [[r[0]-1, r[1]-1] for r in relations]
        dp = [float('inf') for _ in range(2**n)]
        dp[0] = 0
        # 得到 后续课程-先修课程 之间的对应关系
        dic_pre = defaultdict(int) # value=[先修课程]的压缩表示(整数)
        for pre, post in relations:
            dic_pre[post] |= 1 << pre
        for s in range(2 ** n):
            s_nex_all = get_nex_all(s)
            # s_nex_all的子集的集合
            mi_set = get_subset(s_nex_all)
            # 遍历s_nex_all的子集
            for s_nex in mi_set:
                if bin(s_nex)[2:].count('1') <= k:
                    dp[s|s_nex] = min(dp[s|s_nex], dp[s]+1)
        return dp[2 ** n-1]

if __name__ == "__main__":
    n = 4
    dependencies = [[2,1],[3,1],[1,4]]
    k = 2
    sol = Solution()
    result = sol.minNumberOfSemesters(n, dependencies, k)
    print(result)