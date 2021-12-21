'''
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。

在「杨辉三角」中，每个数是它左上方和右上方的数的和。

示例 1:
    输入: rowIndex = 3
    输出: [1,3,3,1]

示例 2:
    输入: rowIndex = 0
    输出: [1]

示例 3:
    输入: rowIndex = 1
    输出: [1,1]
 
提示:
    0 <= rowIndex <= 33

'''

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
    # j 行的数据, 应该由j - 1行的数据计算出来.
    # 假设 j - 1 行为[1,3,3,1], 那么我们前面插入一个0 (j行的数据会比j-1行多一个),
    # 然后执行相加[0+1,1+3,3+3,3+1,1] = [1,4,6,4,1], 最后一个1保留即可.
        res = [1]
        for i in range(1, rowIndex + 1):
            res.insert(0, 0)    # insert(i, elem)
            # 因为i行的数据长度为 i+1 , 所以 j+1 不会越界, 并且最后一个 1 不会被修改.
            for j in range(i):
                res[j] = res[j] + res[j + 1]
        return res

if __name__ == "__main__":
    sol = Solution()
    result = sol.getRow(15)
    print(result)

