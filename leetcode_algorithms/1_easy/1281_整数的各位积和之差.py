"""
https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

给你一个整数 n，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

示例 1：
    输入：n = 234
    输出：15 
    解释：
    各位数之积 = 2 * 3 * 4 = 24 
    各位数之和 = 2 + 3 + 4 = 9 
    结果 = 24 - 9 = 15

示例 2：
    输入：n = 4421
    输出：21
    解释： 
    各位数之积 = 4 * 4 * 2 * 1 = 32 
    各位数之和 = 4 + 4 + 2 + 1 = 11 
    结果 = 32 - 11 = 21

提示：
    1 <= n <= 10^5

"""

'''解法使用eval()函数'''
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return eval("*".join(str(n))) - eval("+".join(str(n)))
        # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
        # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

'''int->str->int'''
class Solution(object):
    def subtractProductAndSum(self, n: int) -> int:
        str_n = str(n)  # 将数字转为字符串
        SUM = 0
        MUL = 1
        for i in range (len(str_n)):
            SUM += int(str_n[i])
            MUL *= int(str_n[i])
        return MUL - SUM

if __name__ == "__main__":
    n = 99999
    sol = Solution()
    result = sol.subtractProductAndSum(n)
    print(result)