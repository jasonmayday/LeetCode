"""
https://leetcode-cn.com/problems/thousand-separator/

给你一个整数 n，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。

示例 1：
    输入：n = 987
    输出："987"

示例 2：
    输入：n = 1234
    输出："1.234"

示例 3：
    输入：n = 123456789
    输出："123.456.789"

示例 4：
    输入：n = 0
    输出："0"

提示：
    0 <= n < 2^31

"""

"""遍历字符串，当在千分位时，在前面加“.”"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        ans = ''
        for i in range(len(s)):
            if i > 0 and (len(s) - i) % 3 == 0:
                ans += '.'
            ans += s[i]
        return ans

"""反转字符串"""
class Solution:
    def thousandSeparator(self, n: int) -> str:
        n = str(n)[::-1]        # 将num转成str型并且进行反转
        new_n = ''
        for i,num in enumerate(n):      # 循环str中的所有字符，每（索引+1）是3的倍数时加上‘.’,最后一位不加。
            new_n+=num
            if (i+1)%3==0 and (i+1)!= len(n):
                new_n+='.'
        return new_n[::-1]

class Solution:
    def thousandSeparator(self, n: int) -> str:
        return format(n,',').replace(',','.')

if __name__ == "__main__":
    n = 123456789
    sol = Solution()
    result = sol.thousandSeparator(n)
    print (result)