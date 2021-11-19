"""
https://leetcode-cn.com/problems/relative-ranks

给出 N 名运动员的成绩，找出他们的相对名次并授予前三名对应的奖牌。前三名运动员将会被分别授予 “金牌”，“银牌” 和“ 铜牌”（"Gold Medal", "Silver Medal", "Bronze Medal"）。

(注：分数越高的选手，排名越靠前。)

示例 1:
    输入: [5, 4, 3, 2, 1]
    输出: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    解释: 前三名运动员的成绩为前三高的，因此将会分别被授予 “金牌”，“银牌”和“铜牌” ("Gold Medal", "Silver Medal" and "Bronze Medal").
    余下的两名运动员，我们只需要通过他们的成绩计算将其相对名次即可。

提示:
    N 是一个正整数并且不会超过 10000。
    所有运动员的成绩都不相同。

"""

from typing import List

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        pairs = []          # 用了一个 pairs 数组，来维护一个 nums -> 索引的映射。
        for i in range(len(nums)):
            pairs.append([nums[i], i])                     # 为每个成绩添加索引，pairs: [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4]]
        pairs.sort(key = lambda a: a[0], reverse = True)   # 对 paris 进行降序排列
        for i in range(len(nums)):
            if i == 0:
                nums[pairs[i][1]] = "Gold Medal"
            if i == 1:
                nums[pairs[i][1]] = "Silver Medal"
            if i == 2:
                nums[pairs[i][1]] = "Bronze Medal"
            if i > 2:
                nums[pairs[i][1]] = str(i + 1)
        return nums

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = sorted([(s, i) for i, s in enumerate(score)], reverse=True)  # 使用enumerate同时获得元素和索引
        for idx, tup in enumerate(rank):                                    # sorted对元组排序时，默认是按照元素的第一个元素排序，所以不需要专门指定
            if idx in [0, 1, 2]:
                score[tup[1]] = medals[idx]
            else:
                score[tup[1]] = str(idx+1)
        return score

if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    sol = Solution()
    result = sol.findRelativeRanks(nums)
    print(result)
