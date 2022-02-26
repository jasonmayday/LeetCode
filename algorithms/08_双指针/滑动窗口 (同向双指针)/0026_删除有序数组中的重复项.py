'''

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
 
示例 1：
    输入：nums = [1,1,2]
    输出：2, nums = [1,2]
    解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例 2：
    输入：nums = [0,0,1,1,1,2,2,3,3,4]
    输出：5, nums = [0,1,2,3,4]
    解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

'''

from typing import List

""" 双指针 """
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1   # 删除重复元素之后也至少剩下一个元素
        while fast < n:
            if nums[fast] != nums[fast - 1]:  # 说明nums[fast] 和之前的元素都不同
                nums[slow] = nums[fast]       # nums[fast] 的值复制到 nums[slow]
                slow += 1
            fast += 1
        
        return slow    # 从nums[0]到nums[slow−1]的每个元素都不相同
    
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol = Solution()
    result = sol.removeDuplicates(nums)
    print(result)