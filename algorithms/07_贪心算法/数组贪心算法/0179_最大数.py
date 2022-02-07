"""
https://leetcode-cn.com/problems/largest-number/

给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
    输入：nums = [10,2]
    输出："210"

示例 2：
    输入：nums = [3,30,34,5,9]
    输出："9534330"

示例 3：
    输入：nums = [1]
    输出："1"

示例 4：
    输入：nums = [10]
    输出："10"

提示：
    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9

"""
from typing import List
from functools import cmp_to_key

""" 方法一：选择排序"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = list(map(str,nums))  # 转换为由字符串组成的数组 ['3', '30', '34', '5', '9']
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:   # 两个数字对应的字符串 a 和 b，如果字典序 a + b > b + a
                    nums[i] = nums[j]   # 此时 a 排在 b 的前面即可获得更大值
                    nums[j] = nums[i]   # 示例：a=3,b=32,两者拼接的值：332>323，所以3应排在32前面
        return str(int("".join(nums)))
    
""" 方法二：cmp_to_key"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x,y):
            return 1 if x + y < y + x else -1
        nums = list(map(str,nums))
        nums.sort(key = cmp_to_key(cmp))
        res = str(int("".join(nums)))
        return res
    
""" 方法三：贪心算法"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str,nums))  # # 转换为由字符串组成的数组 ['3', '30', '34', '5', '9']
        def cmp(a, b):
            if a + b == b + a:
                return 0
            elif a + b > b + a:
                return 1
            else:
                return -1
        strs = sorted(strs, key = cmp_to_key(cmp), reverse = True)  # ['9', '5', '34', '3', '30']
        return ''.join(strs) if strs[0] != '0' else '0'


if __name__ == "__main__":
    nums = [3,30,34,5,9]
    sol = Solution()
    result = sol.largestNumber(nums)
    print(result)