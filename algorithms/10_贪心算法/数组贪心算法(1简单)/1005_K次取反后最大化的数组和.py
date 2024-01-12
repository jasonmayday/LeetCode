"""
https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/

给定一个整数数组 A，我们只能用以下方法修改该数组：
我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选择同一个索引 i。）

以这种方式修改数组后，返回数组可能的最大和。

示例 1：
    输入：A = [4,2,3], K = 1
    输出：5
    解释：选择索引 (1) ，然后 A 变为 [4,-2,3]。

示例 2：
    输入：A = [3,-1,0,2], K = 3
    输出：6
    解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。

示例 3：
    输入：A = [2,-3,-1,5,-4], K = 2
    输出：13
    解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。

提示：
    1 <= A.length <= 10000
    1 <= K <= 10000
    -100 <= A[i] <= 100

"""
from typing import List

''' 贪心算法
    局部最优：让绝对值大的负数变为正数，当前数值达到最大
    整体最优：整个数组和达到最大。'''
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A, key = abs, reverse = True) # 将 A 按绝对值从大到小排列
        for i in range(len(A)):     # 从前向后遍历
            if K > 0 and A[i] < 0:  # 遇到负数将其变为正数
                A[i] *= -1
                K -= 1              # 同时K-1
        if K > 0:                   # 如果K还大于0，那么反复转变数值最小的元素，将K用完
            A[-1] *= (-1)**K        # 取A最后一个数只需要写-1
        return sum(A)
    
''' 多重判断，优先判断0、负数等元素'''
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 思路：先将数组排序，按绝对值大小进行排序，
        # 然后对其循环，遇到一个负数，即反转一次，此时k-1
        # 如果将所有的负数已经反转完了，k还没完，就看有没有0元素，有的话，剩余的k全部用来重复反转0
        # 如果将所有的负数已经反转完了，k还没完，没有0元素，那么就反转最小的绝对值数
        nums.sort()
        i = 0 
        while i < len(nums) :
            if k == 0: # 判断一下，k是不是已经反转完了
                break
            elif nums[i] < 0:   # 反转一个负数，k减1次
                nums[i] *= -1
                k -= 1
                i += 1 
                if k > 0 and i == len(nums) - 1:
                    i = 0
                    continue         
            # 负数转换完了，看是不是有0元素,有的话，就转换0
            elif nums[i] == 0:
                k -= k
                break           
            # 负数转换完了，没有零元素，此时列表全剩正数元素,判断还剩的k是偶数还是奇数
            elif nums[i] > 0:
                lst = sorted(nums , key = abs , reverse = False)
                i = 0
                if k % 2 == 1: # k是奇数            
                    lst[i] *= -1
                    nums = lst
                    k -= k
                    break
                else: # k是偶数
                    k -= k
                    nums = lst
            elif k > 0:
                i = 0
        # 求和
        result = 0
        for i in nums:
            result += i
        return result               


if __name__ == "__main__":      
    A = [2,-3,-1,5,-4]
    K = 2
    sol = Solution()
    result = sol.largestSumAfterKNegations(A,K)
    print(result)