"""
https://leetcode-cn.com/problems/image-smoother/

包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:
    输入:
        [[1,1,1],
        [1,0,1],
        [1,1,1]]
    输出:
        [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
    解释:
        对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
        对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
        对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

注意:
    给定矩阵中的整数范围为 [0, 255]。
    矩阵的长和宽的范围均为 [1, 150]。

"""
from typing import List

"""暴力算法"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        col = len(img[0])
        ans = [[0] * col for _ in range(row)]
        for y in range(row):
            for x in range(col):
                t = count = 0
                for i,j in [(a,b) for a in (y-1, y, y+1) 
                                      for b in (x-1, x, x+1)]:
                    if 0 <= i < row and 0 <= j < col:
                        t += img[i][j]
                        count += 1
                k = t // count
                ans[y][x] = k
        return ans


if __name__ == "__main__":
    img = [[1,1,1],[1,0,1],[1,1,1]]
    sol = Solution()
    result = sol.imageSmoother(img)
    print (result)