"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

示例 1:
    输入: num = 100
    输出: "202"

示例 2:
    输入: num = -7
    输出: "-10"
 
提示：
    -10^7 <= num <= 10^7

"""

'''
10 进制转化任意进制的思路都是除x取余，其中 x 为进制数，比如 2 进制就是 除 2 取余，7 进制就是除 7 取余。

比如一个数 4321 ，需要转化为 7 进制。那么可以：
    先将 4321 除以 7，其中余数为 0 ， 除数为 616
    继续将 616 采用同样的方法直到小于 7
将此过冲的余数反序就是答案了。
'''
# 递归
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7) # 进行辗转相除，每一次除，余数就是该位置的数

# 迭代
class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)
        negative = num < 0
        num = abs(num)
        ans = []
        while num:
            ans.append(str(num % 7))    # 返回两个数相除的余数
            num //= 7                   # 两个数相除，结果为向下取整的整数
        return ("-" if negative else "") + "".join(ans[::-1])

if __name__ == "__main__":
    num = 99999
    sol = Solution()
    result = sol.convertToBase7(num)
    print(result)