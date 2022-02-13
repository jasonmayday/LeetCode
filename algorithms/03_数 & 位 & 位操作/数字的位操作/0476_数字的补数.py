'''
https://leetcode-cn.com/problems/number-complement/

给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

示例 1：
    输入：num = 5
    输出：2
    解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。

示例 2：
    输入：num = 1
    输出：0
    解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

'''

"""方法1：转化为二进制操作"""
class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:] # 转二进制
        res = ''
        for i in range(len(num)):
            if num[i] == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2) # 转十进制
    
"""方法2：位运算"""
class Solution:
    def findComplement(self, num: int) -> int:
        highbit = 0                 # 最高位
        for i in range(1, 30 + 1):  # 最多30位的二进制数字
            if num >= (1 << i):
                highbit = i         # 二进制表示最高位的那个 1
            else:
                break
        
        mask = (1 << (highbit + 1)) - 1
        return num ^ mask

class Solution:
    def findComplement(self, num: int) -> int:
        i = ans = 0
        while num:
            if not num & 1:
                ans += 1 << i
            num >>= 1
            i += 1
        return ans

"""异或"""
class Solution:
    def findComplement(self, num: int) -> int:
        s = num
        begin = 1
        while s > 0:
            begin <<= 1
            s >>= 1
        return num ^ (begin - 1)
    
if __name__ == "__main__":      
    num = 25
    sol = Solution()
    result = sol.findComplement(num)
    print(result)
