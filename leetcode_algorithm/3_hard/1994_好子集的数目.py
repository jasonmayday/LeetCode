"""
https://leetcode-cn.com/problems/the-number-of-good-subsets/

给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。
    
    比方说，如果 nums = [1, 2, 3, 4] ：
        [2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
        [1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。

请你返回 nums 中不同的 好 子集的数目对 109 + 7 取余 的结果。

nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。

示例 1：
    输入：nums = [1,2,3,4]
    输出：6
    解释：好子集为：
        - [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
        - [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
        - [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
        - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
        - [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
        - [3]：乘积为 3 ，可以表示为质数 3 的乘积。

示例 2：
    输入：nums = [4,2,3,15]
    输出：5
    解释：好子集为：
        - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
        - [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
        - [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
        - [3]：乘积为 3 ，可以表示为质数 3 的乘积。
        - [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。

提示：
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 30

"""

import math
from typing import List
from collections import Counter, defaultdict

""" 哈希表 """
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        count = Counter(nums)
        mod = 10 ** 9 + 7
        d = defaultdict(int)
        
        d[1] = (1 << count[1]) % mod
        for num in [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]:
            for x in list(d):
                if math.gcd(num, x) == 1:       # 遍历可能作为好子集元素的数
                    d[num*x] += count[num]*d[x] # 用 哈希表 d 维护能得到的乘积和对应的好子集个数。
                    d[num*x] %= mod             # 可以递推。
        return (sum(d.values())-d[1]) % mod

if __name__ == "__main__":
    nums = [1,2,3,4]
    sol = Solution()
    result = sol.numberOfGoodSubsets(nums)
    print(result)