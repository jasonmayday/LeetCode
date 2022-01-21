"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

说明：

为什么返回数值是整数，但输出的答案是数组呢？

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
    输入：nums = [1,1,1,2,2,3]
    输出：5, nums = [1,1,2,2,3]
    解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

示例 2：
    输入：nums = [0,0,1,1,1,1,2,3,3]
    输出：7, nums = [0,0,1,1,2,3,3]
    解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。

提示：
    1 <= nums.length <= 3 * 10^4
    -10^4 <= nums[i] <= 10^4
    nums 已按升序排列

"""
from typing import List

"""双指针"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0        # 慢指针 slow : 指向当前即将放置元素的位置；则 slow - 1 是刚才已经放置了元素的位置。
        for fast in range(len(nums)):   # 快指针 fast : 向后遍历所有元素；
            if slow < 2 or nums[fast] != nums[slow - 2]:   # 因为最多允许两个重复元素，并且 slow-2 位置是上上次放置了元素的位置，所以让 nums[fast] 跟 nums[slow-2] 进行比较。
                nums[slow] = nums[fast]
                slow += 1
        return slow


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(result)