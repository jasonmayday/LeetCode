"""
https://leetcode-cn.com/problems/detect-squares/

给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
    添加 一个在数据流中的新点到某个数据结构中。可以添加 重复 的点，并会视作不同的点进行处理。
    给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 面积为正 的 轴对齐正方形 ，统计 满足该要求的方案数目。

轴对齐正方形 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。

实现 DetectSquares 类：
    DetectSquares() 使用空数据结构初始化对象
    void add(int[] point) 向数据结构添加一个新的点 point = [x, y]
    int count(int[] point) 统计按上述方式与点 point = [x, y] 共同构造 轴对齐正方形 的方案数。
 

示例：
    输入：
        ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
        [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    输出：
        [null, null, null, null, 1, 0, null, 2]

    解释：
        DetectSquares detectSquares = new DetectSquares();
        detectSquares.add([3, 10]);
        detectSquares.add([11, 2]);
        detectSquares.add([3, 2]);
        detectSquares.count([11, 10]); // 返回 1 。你可以选择：
                                       //   - 第一个，第二个，和第三个点
        detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
        detectSquares.add([11, 2]);    // 允许添加重复的点。
        detectSquares.count([11, 10]); // 返回 2 。你可以选择：
                                       //   - 第一个，第二个，和第三个点
                                       //   - 第一个，第三个，和第四个点

提示：
    point.length == 2
    0 <= x, y <= 1000
    调用 add 和 count 的 总次数 最多为 5000

"""
from typing import List
from collections import Counter
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(Counter)     # 初始化哈希表(字典)

    def add(self, point: List[int]) -> None:
        x, y = point            # 记输入的 point 的横纵坐标分别为 x 和 y
        self.map[y][x] += 1     # 更新该点出现的次数，键必须是不可变变量，所以不能直接用point(列表是可变变量)

    def count(self, point: List[int]) -> int:
        res = 0         # 初始化方案数量
        x, y = point    # 取出该点的横纵坐标

        if not y in self.map:
            return 0
        yCnt = self.map[y]

        for col, colCnt in self.map.items():
            if col != y:
                # 根据对称性，这里可以不用取绝对值
                d = col - y
                res += colCnt[x] * yCnt[x + d] * colCnt[x + d]
                res += colCnt[x] * yCnt[x - d] * colCnt[x - d]
        
        return res
    
if __name__ == "__main__":
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print (detectSquares.count([11, 10]))   # 返回 1 。(你可以选择：第一个，第二个，和第三个点)
    print (detectSquares.count([14, 8]))    # 返回 0 。(查询点无法与数据结构中的这些点构成正方形)
    detectSquares.add([11, 2]);             # 允许添加重复的点。
    print (detectSquares.count([11, 10]))   # 返回 2 。(你可以选择：1. 第一个，第二个，和第三个点   2. 第一个，第三个，和第四个点)