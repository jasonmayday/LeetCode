'''
https://leetcode-cn.com/problems/valid-perfect-square/

给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。

示例 1：
    输入：num = 16
    输出：true

示例 2：
    输入：num = 14
    输出：false
 

提示：
    1 <= num <= 2^31 - 1

'''
# 方法1：暴力
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = 1                    # 如果 num 为完全平方数，那么一定存在正整数 x 满足 x * x = num
        square = 1               # 从 1 开始，从小到大遍历所有正整数，寻找是否存在满足 x * x = num 的正整数 x
        while square <= num:     # 遍历的范围
            if square == num:    # 如果存在 x * x = num，返回 True
                return True
            x += 1
            square = x * x
        return False

# 方法2：二分查找
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid * mid
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False

if __name__ == "__main__":
    num = 16
    sol = Solution()
    result = sol.isPerfectSquare(num)
    print (result) 