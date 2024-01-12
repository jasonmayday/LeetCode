"""
https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/

0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

示例 1：
    输入: n = 5, m = 3
    输出: 3

示例 2：
    输入: n = 10, m = 17
    输出: 2

限制：
    1 <= n <= 10^5
    1 <= m <= 10^6

"""

""" 动态规划
    n-1约瑟夫环的索引index(n-1)                 删除一个数后的n约瑟夫环索引index(n)
                    0               --->                    m % n
                    1               --->                    (m+1)%n
                    2               --->                    (m+2)%n
                    ...                                     ...
                    n-2             --->                    (m+n-2)%n
                    
                    index(n-1)      --->            index(n) = (m+index(n-1))%n
    也就是说，现在的环索引为0的对应原来的索引为3的，换句话说，旧环的索引3跑到新环的索引0位置上了。"""
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        dp = [0 for _ in range(n+1)]  # 设「i,m 问题」的解为 dp[i]
        dp[1] = 0
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + m) % i
        return dp[n]

if __name__ == "__main__":
    n = 5
    m = 3
    sol = Solution()
    result = sol.lastRemaining(n, m)
    print (result)