'''
https://leetcode-cn.com/problems/excel-sheet-column-number/

给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回该列名称对应的列序号。

例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
 
示例 1:
    输入: columnTitle = "A"
    输出: 1

示例 2:
    输入: columnTitle = "AB"
    输出: 28

示例 3:
    输入: columnTitle = "ZY"
    输出: 701

示例 4:
    输入: columnTitle = "FXSHRXW"
    输出: 2147483647
 
提示：
    1 <= columnTitle.length <= 7
    columnTitle 仅由大写英文组成
    columnTitle 在范围 ["A", "FXSHRXW"] 内

'''

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number, multiple = 0, 1
        for i in range(len(columnTitle) - 1, -1, -1):
            k = ord(columnTitle[i]) - ord("A") + 1
            number += k * multiple
            multiple *= 26
        return number


if __name__ == "__main__":
    columnTitle = "FXSHRXW"
    sol = Solution()
    result = sol.titleToNumber(columnTitle)
    print(result)
