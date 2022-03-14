"""
https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists/

假设Andy和Doris想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设总是存在一个答案。

示例 1:
    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    输出: ["Shogun"]
    解释: 他们唯一共同喜爱的餐厅是“Shogun”。

示例 2:
    输入:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    输出: ["Shogun"]
    解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。

提示:
    两个列表的长度范围都在 [1, 1000]内。
    两个列表中的字符串的长度将在[1，30]的范围内。
    下标从0开始，到列表的长度减1。
    两个列表都没有重复的元素。

"""
from typing import List
from collections import defaultdict

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = defaultdict(list)        # key为字符串，value为出现的下标
        for i in range(len(list1)):     # 把 list1 每个字符串对应的索引入字典
            dict[list1[i]].append(i)
        for i in range(len(list2)):     # 把 list2 每个字符串对应的索引入字典
            dict[list2[i]].append(i)
        # print(dict) {'Shogun': [0, 1], 'Tapioca Express': [1], 'Burger King': [2, 2], 'KFC': [3, 0]})
        min_index = float("inf")
        result = []
        for key, value in dict.items():     # 遍历求两个value[0] + value[1]的和最小的str
            if len(value) == 2:             # 出现超过一次，说明两个人都喜欢
                if value[0] + value[1] < min_index:
                    result = []
                    min_index = value[0] + value[1]
                    result.append(key)
                elif value[0] + value[1] == min_index:
                    result.append(key)
        return result
    
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {index: i for i, index in enumerate(list1)}
        # index: {'Shogun': 0, 'Tapioca Express': 1, 'Burger King': 2, 'KFC': 3}
        ans = []
        indexSum = float("inf")
        for i, s in enumerate(list2):
            if s in index:
                j = index[s]
                if i + j < indexSum:
                    indexSum = i + j
                    ans = [s]
                elif i + j == indexSum:
                    ans.append(s)
        return ans

class Solution:
    def findRestaurant(self, list1, list2):
        index1 = {list1[i]: i for i in range(len(list1))}
        index2 = {list2[i]: i for i in range(len(list2))}
        agreements = set(list1) & set(list2)
        sum_index = {r: index1[r]+index2[r] for r in agreements}
        return [r for r in agreements if sum_index[r] == min(sum_index.values())]

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in dict if dict[x] == min(dict.values())]

if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    sol = Solution()
    result = sol.findRestaurant(list1, list2)
    print(result)