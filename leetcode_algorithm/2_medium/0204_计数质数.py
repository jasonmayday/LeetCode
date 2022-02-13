"""
https://leetcode-cn.com/problems/count-primes/

给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。

示例 1：
    输入：n = 10
    输出：4
    解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

示例 2：
    输入：n = 0
    输出：0

示例 3：
    输入：n = 1
    输出：0

提示：
    0 <= n <= 5 * 10^6

"""

""" 厄拉多塞筛法. 
    比如说求20以内质数的个数，首先0,1不是质数。
    2 是第一个质数，然后把20以内所有2的倍数划去。
    2 后面紧跟的数即为下一个质数 3，然后把 3 所有的倍数划去。
    3 后面紧跟的数即为下一个质数 5，再把 5 所有的倍数划去。以此类推。"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0     

        output = [1] * n                # 首先生成了一个全部为1的列表
        output[0], output[1] = 0, 0     # 因为0和1不是质数,所以列表的前两个位置赋值为0
            
        
        for i in range(2, int(n**0.5) + 1):     # 从index = 2开始遍历（2到根号n）
            if output[i] == 1:                  # output[2] == 1, 即表明第一个质数为 2
                output[i*i:n:i] = [0] * len(output[i*i:n:i])    # 然后将 2 的倍数对应的索引全部赋值为 0（排除 2 的倍数）
                                                                # 此时output[3] == 1, 即表明下一个质数为3, 同样划去3的倍数.  以此类推.
                                                                # 要排除的是所有小于等于根号n的质数的倍数，而不是所有小于等于根号n的数的倍数. n = 100 时，排除到根号100，也就是10
        return sum(output)  # 最后output中的数字1表明该位置上的索引数为质数,然后求和即可.
    
if __name__ == "__main__":
    n = 100
    sol = Solution()
    result = sol.countPrimes(n)
    print (result)