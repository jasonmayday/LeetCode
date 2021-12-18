"""
https://leetcode-cn.com/problems/build-an-array-with-stack-operations/

给你一个目标数组 target 和一个整数 n。每次迭代，需要从  list = {1,2,3..., n} 中依序读取一个数字。

请使用下述操作来构建目标数组 target ：

Push：从 list 中读取一个新元素， 并将其推入数组中。
Pop：删除数组中的最后一个元素。
如果目标数组构建完成，就停止读取更多元素。
题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。

请返回构建目标数组所用的操作序列。

题目数据保证答案是唯一的。

示例 1：
    输入：target = [1,3], n = 3
    输出：["Push","Push","Pop","Push"]
    解释： 
    读取 1 并自动推入数组 -> [1]
    读取 2 并自动推入数组，然后删除它 -> [1]
    读取 3 并自动推入数组 -> [1,3]

示例 2：
    输入：target = [1,2,3], n = 3
    输出：["Push","Push","Push"]

示例 3：
    输入：target = [1,2], n = 4
    输出：["Push","Push"]
    解释：只需要读取前 2 个数字就可以停止。

示例 4：
    输入：target = [2,3,4], n = 4
    输出：["Push","Pop","Push","Push","Push"]

提示：
    1 <= target.length <= 100
    1 <= target[i] <= 100
    1 <= n <= 100
    target 是严格递增的

"""
from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        for num in list(range(1, max(target)+1)):
            if num not in target:
                res.extend(["Push","Pop"])
            else:
                res.append("Push")
        return res


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        tmp = []  # 新建数组，用于与目标数组比较
        i = 1  # 元素值
        j = 0  # 目标数组索引
        while i < n+1:
            # 判断res与目标数组是否一致
            if tmp == target:
                return res
            # 对每一个数先执行推入操作
            res.append('Push')
            tmp.append(i)
            # 若该数不存在于目标数组再推出
            if tmp[-1] != target[j]:
                res.append('Pop')
                tmp.pop()
            else:
                j += 1
            i += 1
        return res


if __name__ == "__main__":
    target = [1,3]
    n = 3
    sol = Solution()
    result = sol.buildArray(target, n)
    print(result)