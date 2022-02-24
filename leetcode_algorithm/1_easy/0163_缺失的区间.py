"""
https://leetcode-cn.com/problems/missing-ranges/

给定一个排序的整数数组 nums ，其中元素的范围在 闭区间 [lower, upper] 当中，返回不包含在数组中的缺失区间。

示例：
    输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
    输出: ["2", "4->49", "51->74", "76->99"]

"""

""" 双指针
    使用双指针low、num，遍历nums添加对应范围即可；"""
class Solution:
    def findMissingRanges(self, nums: int, lower: int, upper: int) -> str:
        res = []
        low = lower - 1
        nums.append(upper + 1)  # 添加终止边界
        for num in nums:
            dif = num - low
            if dif == 2:                    # 非区间
                res.append(str(low + 1))
            elif dif > 2:                   # 区间
                res.append(str(low + 1) + "->" + str(num - 1))
            low = num
        return res

if __name__ == "__main__":
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    sol = Solution()
    result = sol.findMissingRanges(nums, lower, upper)
    print(result)