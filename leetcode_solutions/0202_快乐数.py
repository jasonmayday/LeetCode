'''
https://leetcode-cn.com/problems/happy-number/

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：
    对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
    然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
    如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 true ；不是，则返回 false 。

示例 1：
    输入：19
    输出：true
    解释：
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1

示例 2：
    输入：n = 2
    输出：false

'''

class Solution:
    def isHappy(self, n: int) -> bool:  
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)      # divmod(a,b)返回 a/b 的商和余数
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

if __name__ == "__main__":
    n = 19
    sol = Solution()
    result = sol.isHappy(n)
    print (result)  