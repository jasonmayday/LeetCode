"""
https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/

给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。

如果存在 k 同时满足 k <= li 和 k <= wi ，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 4 的正方形。

设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。

请你统计有多少个矩形能够切出边长为 maxLen 的正方形，并返回矩形 数目 。

示例 1：
    输入：rectangles = [[5,8],[3,9],[5,12],[16,5]]
    输出：3
    解释：能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
    最大正方形的边长为 5 ，可以由 3 个矩形切分得到。

示例 2：
    输入：rectangles = [[2,3],[3,7],[4,3],[3,7]]
    输出：3

提示：
    1 <= rectangles.length <= 1000
    rectangles[i].length == 2
    1 <= li, wi <= 10^9
    li != wi

"""
from typing import List
from collections import Counter

""" [[5,8],[3,9],[5,12],[16,5]] """

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rec = [min(i) for i in rectangles]    # 先把所有正方形都找到
        return rec.count(max(rec))            # 然后计算最大值的个数即可

    
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        return sorted(Counter(min(rec) for rec in rectangles).items(), key = lambda item: item[0], reverse = True)[0][1]


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        max_edge = 0
        for i, j in rectangles:
            edge = min([i,j])
            if edge > max_edge:
                count = 1
                max_edge = edge
            elif edge == max_edge:
                count +=1
        return count


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        edges = []
        for x in rectangles:
            if x[0] < x[1]:
                edges.append(x[0])
            else:
                edges.append(x[1])
        edges.sort(reverse = True)      # 从大到小排列
        return edges.count(edges[0])    # 返回最大值的个数


if __name__ == "__main__":
    rectangles = [[5,8],[3,9],[5,12],[16,5]]
    sol = Solution()
    result = sol.countGoodRectangles(rectangles)
    print(result)