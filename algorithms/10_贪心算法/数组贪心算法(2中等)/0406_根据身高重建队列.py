"""
https://leetcode-cn.com/problems/queue-reconstruction-by-height/

假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。

请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第 j 个人的属性（queue[0] 是排在队列前面的人）。

示例 1：
    输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    解释：
    编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
    编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
    编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
    编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
    编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
    编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
    因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

示例 2：
    输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

提示：
    1 <= people.length <= 2000
    0 <= hi <= 10^6
    0 <= ki < people.length
    题目数据确保队列可以被重建

"""

""" 先对输入数组排序，h升序，k降序
    从头循环遍历 当前这个人就是剩下未安排的人中最矮的人，他的k值就代表他在剩余空位的索引值 如果有多个人高度相同，要按照k值从大到小领取索引值 示例：
    [ 0, 1, 2, 3, 4, 5 ] [ 4, 4 ] 4
    [ 0, 1, 2, 3, 5 ]    [ 5, 2 ] 2
    [ 0, 1, 3, 5 ]       [ 5, 0 ] 0
    [ 1, 3, 5 ]          [ 6, 1 ] 3
    [ 1, 5 ]             [ 7, 1 ] 5
    [ 1 ]                [ 7, 0 ] 1
    [ [ 5, 0 ], [ 7, 0 ], [ 5, 2 ], [ 6, 1 ], [ 4, 4 ], [ 7, 1 ] ]
"""
from typing import List

""" 贪心：从低到高考虑 """
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (x[0], -x[1]))
        print('people: ', people)
        # [[4, 4], [5, 2], [5, 0], [6, 1], [7, 1], [7, 0]]
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans

""" 贪心：从高到低考虑
    for 循环实现，额外 res 数组空间存储 """
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people = sorted(people, key = lambda x: (-x[0], x[1]))  # 元素 1 降序排序，元素 2 升序排序
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        for p in people:
            if len(res) <= p[1]:    # 如果当前答案的长度小于遍历到的人的元素 2
                res.append(p)       # 直接插入res的尾部
            elif len(res) > p[1]:   # 如果当前答案的长度大于遍历到的人的元素 2
                res.insert(p[1], p) # 插入到res的 index = p[1] 的位置
        return res
    
""" 贪心：从高到低考虑
    while 循环实现，原地改变 """
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        i = 0
        while i < len(people):
            if i > people[i][1]:
                people.insert(people[i][1], people[i])
                people.pop(i+1)
            i += 1
        return people

if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    sol = Solution()
    result = sol.reconstructQueue(people)
    print (result)