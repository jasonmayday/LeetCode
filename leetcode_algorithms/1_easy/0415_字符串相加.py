"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

示例 1：
    输入：num1 = "11", num2 = "123"
    输出："134"

示例 2：
    输入：num1 = "456", num2 = "77"
    输出："533"

示例 3：
    输入：num1 = "0", num2 = "0"
    输出："0"

提示：
    1 <= num1.length, num2.length <= 10^4
    num1 和num2 都只包含数字 0-9
    num1 和num2 都不包含任何前导零

"""

'''双指针'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1)-1     # 指针 i 指向num1尾部，模拟人工加法
        j = len(num2)-1     # 指针 j 指向num1尾部
        res = ""
        carry = 0
        while i >=0 or j >= 0:
            n1 = num1[i] if i >= 0 else '0'     # n1 为 num1 当前计算位
            n2 = num2[j] if j >= 0 else '0'     # n2 为 num2 当前计算位
            temp = ord(n1) + ord(n2) - 2 * ord('0') + carry   # 添加当前位
            cur = temp % 10 
            carry = temp // 10      # 计算代表当前位相加是否产生进位，如果进位，carry = 1
            res = chr(cur + 48) + res
            i -= 1
            j -= 1 
        return '1' + res if carry != 0 else res

if __name__ == "__main__":
    num1 = "51189"
    num2 = "967895"
    sol = Solution()
    result = sol.addStrings(num1,num2)
    print (result)  
