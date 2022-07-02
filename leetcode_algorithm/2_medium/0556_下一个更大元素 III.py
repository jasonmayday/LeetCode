"""
https://leetcode.cn/problems/next-greater-element-iii/

给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

示例 1：
    输入：n = 12
    输出：21

示例 2：
    输入：n = 21
    输出：-1

提示：
    1 <= n <= 2^31 - 1

"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = [int(x) for x in str(n)] # [1, 2, 3]
        if sorted(nums)[::-1] == nums:
            return -1
        m = len(nums)
        # 从右往左遍历 找到第一个不是顺序排列的数字,而不是第一个比最右的数小的数
        for i in range(m - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(m - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:])
                        break
                break
        res = 0
        for i in nums:
            res = 10 * res + i
        if res < 2 ** 31:
            return res
        else:
            return -1
    
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))     # ["1", "2", "3"]
        
        i = len(nums) - 2       # i = 1，下标从倒数第二个数字开始
        while i >= 0 and nums[i] >= nums[i + 1]:    # 左边数字大于右边数字
            i -= 1                                  # 每出现一次左边数字大于右边数字，i减一
        if i < 0:           # 当 i < 0时，说明检查完，该数字从左到右每一位都在递减，
            return -1       # 所以无法找到需要的结果，返回 -1
                            # 遍历结束后，i就是最右边的可以交换的组合（左边数字小于右边数字）
        
        j = len(nums) - 1       # j = 1，下标从倒数第一个数字开始
        while j >= 0 and nums[i] >= nums[j]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]
        ans = int(''.join(nums))
        return ans if ans < 2 ** 31 else -1

if __name__ == "__main__":
    n = 123
    sol = Solution()
    result = sol.nextGreaterElement(n)
    print (result)