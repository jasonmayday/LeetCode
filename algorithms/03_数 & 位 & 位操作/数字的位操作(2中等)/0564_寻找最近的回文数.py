"""
https://leetcode-cn.com/problems/find-the-closest-palindrome/

给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数差的绝对值最小。

示例 1:
    输入: n = "123"
    输出: "121"

示例 2:
    输入: n = "1"
    输出: "0"
    解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。

提示:
    1 <= n.length <= 18
    n 只由数字组成
    n 不含前导 0
    n 代表在 [1, 1018 - 1] 范围内的整数

"""

class Solution:
    """ 函数: 取字符串前一半镜像成回文串 """
    def mirror(self, n:str):
        length = len(n)
        half = length // 2
        if length % 2 == 0:                                 # 如果偶数个字符
            return n[:half] + ''.join(reversed(n[:half]))   # 直接取前一半，然后加上前一半的翻转
        else:                                               # 如果奇数个字符
            return n[:half+1] + ''.join(reversed(n[:half])) # 取前一半，然后加上前一半的翻转，中间字符不变

    """ 函数: 得到一个小于原数的回文 """
    def get_small(self, n:str):
        half = len(n) // 2
        if len(n) % 2 == 0:
            half -= 1
        half_num = int (n[:half+1])
        half_str = str (half_num-1)
        if half_str == '0' or len(half_str) < half + 1:
            return '9'*(len(n)-1)
        else:
            return self.mirror(half_str+n[half+1:])

    """ 函数: 得到一个大于原数的回文 """
    def get_big(self, n:str):
        half = len(n) // 2
        if len(n) % 2 == 0:
            half -= 1
        half_num = int (n[:half+1])
        half_str = str (half_num+1)

        return self.mirror(half_str+n[half+1:])

    """ 主函数: 返回与它最近的回文整数 """
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        if n == 0:
            return "1"
        if num < 10:
            return str(num - 1)

        palindromic_str = self.mirror(n)        # 先取前一半（N）镜像成回文串，跟原数做比较
        palindromic_num = int(palindromic_str)

        if palindromic_num > num:               # 如果大于原数
            small_num = int(self.get_small(n))
            big_num = palindromic_num

        elif palindromic_num < num:             # 如果小于原数
            small_num = palindromic_num
            big_num = int(self.get_big(n))

        else:
            small_num = int(self.get_small(n))
            big_num = int(self.get_big(n))

        if abs(big_num - num) < abs(small_num - num):
            return str(big_num)
        else:
            return str(small_num)

if __name__ == "__main__":
    n = "123"
    sol = Solution()
    result = sol.nearestPalindromic(n)
    print(result)