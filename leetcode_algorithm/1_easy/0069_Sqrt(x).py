'''
https://leetcode-cn.com/problems/sqrtx/

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

示例 1：
    输入：x = 4
    输出：2

示例 2：
    输入：x = 8
    输出：2
    解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

提示：
    0 <= x <= 2^31 - 1

'''

""" 解法1：梯度下降"""
class Solution:
    def mySqrt(self, x: int) -> int:
        t = 1
        lr = 0.0001    # learning_rate 学习率
        
        # 求解的表达式 x= f(t) = t*t
        # 用mse均方差损失函数 loss = (f(t)-x)^2 定义精度
        # 不需要正则化项，所以目标函数就是损失函数 loss = (f(t)-x)^2
        
        while (x - t**2) ** 2 > 0.01:
            # 迭代过程 t(n) = t(n-1) - lr * (d((f(t)-x)^2)/d(t))
            # 损失函数对t求偏导，x是常数
            # 2(f(t)-x) 乘以 f(t) 对 t 的导数，也就是 2t，偏导部分为：(4*t*(t*t-x)) 
            t = t - lr * (4*t*(t*t-x)) 
        
        if (int(t)+1) ** 2 <= x:    # int(t)+1 为 t 向上取整之后的值，平方后是否可以小于等于 x，如果可以就返回向上取整之后的值
            return int(t) + 1       # 比如: 4 通过梯度下降以后得到的值是 1.97，(int(t)+1) = 2，2^2 =4，我们要返回 2。
        else:                       # 如果不行就返回向下取整的值
            return int(t)           # 比如: 8 通过梯度下降之后是 2.8，(int(t)+1) = 3， 3^2 > 8，我们要返回 2


""" 解法2：二分查找"""
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x   # 二分查找的下界为 0，上界可以粗略地设定为 x
        ans = -1
        while left <= right:
            mid = (left + right) // 2   # 比较中间元素 mid 的平方与 x 的大小关系
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    x = 4
    sol = Solution()
    result = sol.mySqrt(x)
    print(result)