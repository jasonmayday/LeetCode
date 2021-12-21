"""
https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

给你一个下标从 0 开始的整数数组 nums ，如果 恰好 删除 一个 元素后，数组 严格递增 ，那么请你返回 true ，否则返回 false 。如果数组本身已经是严格递增的，请你也返回 true 。

数组 nums 是 严格递增 的定义为：对于任意下标的 1 <= i < nums.length 都满足 nums[i - 1] < nums[i] 。

示例 1：
    输入：nums = [1,2,10,5,7]
    输出：true
    解释：从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
    [1,2,5,7] 是严格递增的，所以返回 true 。

示例 2：
    输入：nums = [2,3,1,2]
    输出：false
    解释：
    [3,1,2] 是删除下标 0 处元素后得到的结果。
    [2,1,2] 是删除下标 1 处元素后得到的结果。
    [2,3,2] 是删除下标 2 处元素后得到的结果。
    [2,3,1] 是删除下标 3 处元素后得到的结果。
    没有任何结果数组是严格递增的，所以返回 false 。

示例 3：
    输入：nums = [1,1,1]
    输出：false
    解释：删除任意元素后的结果都是 [1,1] 。
    [1,1] 不是严格递增的，所以返回 false 。

示例 4：
    输入：nums = [1,2,3]
    输出：true
    解释：[1,2,3] 已经是严格递增的，所以返回 true 。

提示：
    2 <= nums.length <= 1000
    1 <= nums[i] <= 1000

"""
from typing import List

"""解法1：使用集合判断重复"""
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if sorted(nums[:i] + nums[i+1:]) == nums[:i] + nums[i+1:] and len(set(nums[:i] + nums[i+1:])) == len(nums) - 1:
                return True
            # sorted(nums[:i]+nums[i+1:]) == nums[:i]+nums[i+1:]  存在一个数 num[i]，它之前和之后的数组拼在一起递增（但不是严格递增）
            # len(set(nums[:i]+nums[i+1:])) == len(nums)-1        存在一个数 num[i]，数组除去它以后其他的数字没有重复（因此严格递增）
        return False

"""解法2：双指针"""
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        pre = nums[0]   # 慢指针从第一位开始
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= pre:          # 如果某一位比之前数值小
                count += 1              # 计数加一
                if count > 1:           # 如果出现两次某位比之前数值小
                    return False        # 返回False
                if i > 1 and nums[i] <= nums[i - 2]:
                    pre = nums[i - 1]   # 慢指针 pre 一直维护下一次应该比较的数
                else:
                    pre = nums[i]
            else:
                pre = nums[i]
        return count <= 1

if __name__ == "__main__":
    nums = [1,2,10,5,7]
    sol = Solution()
    result = sol.canBeIncreasing(nums)
    print (result)