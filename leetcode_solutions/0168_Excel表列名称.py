'''
https://leetcode-cn.com/problems/excel-sheet-column-title/

给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。

例如：
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

示例 1：
    输入：columnNumber = 1
    输出："A"

示例 2：
    输入：columnNumber = 28
    输出："AB"

示例 3：
    输入：columnNumber = 701
    输出："ZY"

示例 4：
    输入：columnNumber = 2147483647
    输出："FXSHRXW"
 

提示：
    1 <= columnNumber <= 2^31 - 1

'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        # 10 进制转换为 26 进制，A对应1，B对应2,....Z对应26；27的excel列表名称是AA
        while columnNumber > 0:
            columnNumber -= 1                           # 最右边位为取模运算的结果
            ans.append(chr(columnNumber%26 + ord("A"))) # A 的 ASC 码 65，ord("A") = 65
            columnNumber //= 26
        return ''.join(ans[::-1])       # 由于我们计算列名称的顺序是从右往左，因此需要将拼接后的结果反转

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        return self.convertToTitle((columnNumber-1)//26) + chr((columnNumber-1)%26 + 65) if columnNumber > 0 else ''

if __name__ == "__main__":
    columnNumber = 2147483647
    sol = Solution()
    result = sol.convertToTitle(columnNumber)
    print(result)