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

class Solution:
    def findComplement(self, num: int) -> int:
        num = bin(num)[2:] # 转二进制
        res = ''
        for i in range(len(num)):
            if num[i] == '0':res += '1'
            else: res += '0'
        return int(res,2) # 转十进制

if __name__ == "__main__":      
    num = 78
    sol = Solution()
    result = sol.findComplement(num)
    print(result)
