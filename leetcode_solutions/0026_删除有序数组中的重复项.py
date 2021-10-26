'''
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
 
示例 1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 
提示：
0 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按升序排列

'''
nums = [0,0,1,1,1,2,2,3,3,4]

# 我们只能在原地修改nums数组，不能创建新的数组空间来存储删除重复出现的元素后的结果。
# 我们需要一边遍历数组查找相同元素，一边在对比发现不同元素时修改数组元素。

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1  # 初始化时指针slow指向数组的起始位置 nums[0]，指针fast指向指针slow的后一个位置 nums[1]
        while fast < len(nums):
            if nums[fast] != nums[slow]: 
                slow = slow + 1
                nums[slow] = nums[fast]  # 如果 nums[fast] = nums[slow]
            fast = fast + 1              # 指针fast继续向后查找
        return slow + 1

sol = Solution()
result = sol.removeDuplicates(nums)
print(result)