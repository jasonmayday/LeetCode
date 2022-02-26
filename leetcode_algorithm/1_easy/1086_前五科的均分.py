"""
https://leetcode-cn.com/problems/high-five/

给你一个不同学生的分数列表 items，其中 items[i] = [IDi, scorei] 表示 IDi 的学生的一科分数，你需要计算每个学生 最高的五科 成绩的 平均分。

返回答案 result 以数对数组形式给出，其中 result[j] = [IDj, topFiveAveragej] 表示 IDj 的学生和他 最高的五科 成绩的 平均分。result 需要按 IDj  递增的 顺序排列 。

学生 最高的五科 成绩的 平均分 的计算方法是将最高的五科分数相加，然后用 整数除法 除以 5 。

示例 1：
    输入：items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    输出：[[1,87],[2,88]]
    解释：
        ID = 1 的学生分数为 91、92、60、65、87 和 100 。前五科的平均分 (100 + 92 + 91 + 87 + 65) / 5 = 87
        ID = 2 的学生分数为 93、97、77、100 和 76 。前五科的平均分 (100 + 97 + 93 + 77 + 76) / 5 = 88.6，但是由于使用整数除法，结果转换为 88

示例 2：
    输入：items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
    输出：[[1,100],[7,100]]

提示：
    1 <= items.length <= 1000
    items[i].length == 2
    1 <= IDi <= 1000
    0 <= scorei <= 100
    对于每个 IDi，至少 存在五个分数

"""
from typing import List
from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        student_scores = defaultdict(list)
        for student, scores in items:
            student_scores[student].append(scores)   # {1: [91, 92, 60, 65, 87, 100], 2: [93, 97, 77, 100, 76]}
        res = []
        for stu, scores in student_scores.items():
            scores.sort()
            avg = sum(scores[-5: ]) // 5
            res.append([stu, avg])
        res.sort(key = lambda x: x[0])
        return res

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(key = lambda items:[items[0], items[1]], reverse = True)
        # 对分数列表进行排序，以id为主要关键字，分数为次要关键字，并从高到低
        # [[2, 100], [2, 97], [2, 93], [2, 77], [2, 76], [1, 100], [1, 92], [1, 91], [1, 87], [1, 65], [1, 60]]
        res = []
        dic = {}
        for student, scores in items:
            if student in dic:
                if dic[student] < 5:
                    dic[student] = dic.get(student) + 1 # 对相同id的分数列表进行累加
                    res[-1][1] += scores
            else:
                dic[student] = dic.get(student, 0) + 1
                res.append([student, scores])
        for i in range(len(res)): res[i][1] = res[i][1]//dic[res[i][0]]
        res.reverse()
        return res

if __name__ == "__main__":
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    sol = Solution()
    result = sol.highFive(items)
    print(result)