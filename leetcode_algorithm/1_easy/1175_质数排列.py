"""
https://leetcode-cn.com/problems/prime-arrangements/

请你帮忙给从 1 到 n 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 模 mod 10^9 + 7 之后的结果即可。

示例 1：
    输入：n = 5
    输出：12
    解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

示例 2：
    输入：n = 100
    输出：682289015
 
提示：
    1 <= n <= 100

"""

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        cnt_prime = 0 # 质数的个数
        sum_prime = 1 # 质数的个数全排列和
        
        cnt_np = 1 # 非质数的个数
        sum_np = 1 # 非质数的个数全排列的和
         
        for i in range(2, n + 1): 
            if self.isPrime(i):
                cnt_prime += 1
                sum_prime *= cnt_prime
            else:
                cnt_np += 1
                sum_np *= cnt_np
        
        #质数个数的全排列 * 非质数个数的全排列
        return (sum_prime * sum_np) % (10**9 + 7)
        
    def isPrime(self, num: int) -> bool:
        i = 2
        while i * i <= num:
            if num % i == 0:
                return False
            i += 1
        return True
    
if __name__ == "__main__":
    n = 100
    sol = Solution()
    result = sol.numPrimeArrangements(n)
    print(result)