"""
https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/

统计一个数字在排序数组中出现的次数。

示例 1:
    输入: nums = [5,7,7,8,8,10], target = 8
    输出: 2

示例 2:
    输入: nums = [5,7,7,8,8,10], target = 6
    输出: 0

提示：
    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums 是一个非递减数组
    -10^9 <= target <= 10^9

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

"""
from typing import List

""" 二分查找"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1     # 利用两次二分法分别确定target的左右边界
        
        # 第一次二分：找右边界
        while i <= j:               # 当闭区间[i,j] 无元素时跳出
            m = (i + j) // 2        # 计算中点
            if nums[m] <= target:   # 这里是“小于等于”，目的是为了确定右边界，就是说当mid等于target时，因为不确定后面还有没有target，所以同样需要左边收缩范围
                i = m + 1           # 目标在中点右边 [m+1,j] 中，因此缩小左边界，执行 i=m+1
            else:                   # 中点值大于目标值
                j = m - 1           # 目标在中点左边 [i,m−1] 中，因此缩小右边界，执行 j=m-1
        right = i   # 更新右边界
        
        if j >= 0 and nums[j] != target:    # 若数组中无 target ，则提前返回
            return 0
        
        # 第二次二分：找左边界
        i = 0       # 更新左指针
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j    # 更新左边界
        return right - left - 1     # 左右边界为target值序列的左/右一位，因此最终结果是right-left-1

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    sol = Solution()
    result = sol.search(nums, target)
    print (result)