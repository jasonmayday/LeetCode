"""
https://leetcode.cn/problems/merge-similar-items/

给你两个二维整数数组 items1 和 items2 ，表示两个物品集合。每个数组 items 有以下特质：

    items[i] = [valuei, weighti] 其中 valuei 表示第 i 件物品的 价值 ，weighti 表示第 i 件物品的 重量 。
    items 中每件物品的价值都是 唯一的 。
请你返回一个二维数组 ret，其中 ret[i] = [valuei, weighti]， weighti 是所有价值为 valuei 物品的 重量之和 。

注意：ret 应该按价值 升序 排序后返回。

示例 1：
    输入：items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]
    输出：[[1,6],[3,9],[4,5]]
    解释：
    value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 5 ，总重量为 1 + 5 = 6 。
    value = 3 的物品再 items1 中 weight = 8 ，在 items2 中 weight = 1 ，总重量为 8 + 1 = 9 。
    value = 4 的物品在 items1 中 weight = 5 ，总重量为 5 。
    所以，我们返回 [[1,6],[3,9],[4,5]] 。

示例 2：
    输入：items1 = [[1,1],[3,2],[2,3]], items2 = [[2,1],[3,2],[1,3]]
    输出：[[1,4],[2,4],[3,4]]
    解释：
    value = 1 的物品在 items1 中 weight = 1 ，在 items2 中 weight = 3 ，总重量为 1 + 3 = 4 。
    value = 2 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 1 ，总重量为 3 + 1 = 4 。
    value = 3 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
    所以，我们返回 [[1,4],[2,4],[3,4]] 。

示例 3：
    输入：items1 = [[1,3],[2,2]], items2 = [[7,1],[2,2],[1,4]]
    输出：[[1,7],[2,4],[7,1]]
    解释：
    value = 1 的物品在 items1 中 weight = 3 ，在 items2 中 weight = 4 ，总重量为 3 + 4 = 7 。
    value = 2 的物品在 items1 中 weight = 2 ，在 items2 中 weight = 2 ，总重量为 2 + 2 = 4 。
    value = 7 的物品在 items2 中 weight = 1 ，总重量为 1 。
    所以，我们返回 [[1,7],[2,4],[7,1]] 。

提示：
    1 <= items1.length, items2.length <= 1000
    items1[i].length == items2[i].length == 2
    1 <= valuei, weighti <= 1000
    items1 中每个 valuei 都是 唯一的 。
    items2 中每个 valuei 都是 唯一的 。

"""
from typing import List
from collections import Counter

"""使用字典来保存items1和items2这两个嵌套列表，然后把字典变成列表，并排序"""
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in items1:
            dic[i[0]] = i[1]
        for i in items2:
            if i[0] in dic:
                dic[i[0]] += i[1]
            else:
                dic[i[0]] = i[1]
        # 字典变列表
        res = []
        for k, v in dic.items():
            res.append([k, v])
        res.sort()
        return res

"""哈希：使用数组来保存信息"""
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # 使用数组求解
        List = [0] * 2000
        for i in items1:
            List[i[0]] = List[i[0]] + i[1]
        for i in items2:
            List[i[0]] = List[i[0]] + i[1]
        ans = []
        for i in range(len(List)):
            if List[i] != 0:
                ans.append([i, List[i]])
        return ans

"""Counter，但是返回的其实是嵌套的二元组"""
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return sorted((Counter(dict(items1)) + Counter(dict(items2))).items())

if __name__ == "__main__":
    items1 = [[1,1],[4,5],[3,8]]
    items2 = [[3,1],[1,5]]
    sol = Solution()
    result = sol.mergeSimilarItems(items1, items2)
    print (result)