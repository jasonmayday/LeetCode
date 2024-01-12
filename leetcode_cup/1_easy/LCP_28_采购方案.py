"""
https://leetcode-cn.com/problems/4xy4Wx/

小力将 N 个零件的报价存于数组 nums。小力预算为 target，假定小力仅购买两个零件，要求购买零件的花费不超过预算，请问他有多少种采购方案。

注意：答案需要以 1e9 + 7 (1000000007) 为底取模，如：计算初始结果为：1000000008，请返回 1

示例 1：
    输入：nums = [2,5,3,5], target = 6
    输出：1
    解释：预算内仅能购买 nums[0] 与 nums[2]。

示例 2：
    输入：nums = [2,2,1,9], target = 10
    输出：4
    解释：符合预算的采购方案如下：
        nums[0] + nums[1] = 4
        nums[0] + nums[2] = 3
        nums[1] + nums[2] = 3
        nums[2] + nums[3] = 10

提示：
    2 <= nums.length <= 10^5
    1 <= nums[i], target <= 10^5

"""

from typing import List

"""在 numsnums 中找到两个数 a 和 b，并且让其满足 a + b <= target 即可"""
class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()         # 先对 nums 做升序排序。[1,2,2,9]
        ans = 0
        i = 0               # 指针 i 指针指向 nums 首位
        j = len(nums)-1     # 再创建一个指针 j 指向 nums 末位
        while i < j:
            if nums[i] + nums[j] > target:  # 不满足条件
                j -= 1                      # j 指针左移一位
            else:               # 满足条件，既然该范围的边界值之和都满足了条件，那么代表该区间内的所有数字和 nums[i] 相加都满足条件
                ans += (j - i)  # 所以，我们可以通过 j−i 来获取到当前有多少个数，可以和 nums[i] 相加后满足条件
                i += 1          # i 指针右移一位
        if ans <= 1000000007:
            return ans
        else:
            return ans % 1000000007

if __name__ == "__main__":
    nums = [2,2,1,9]
    target = 10
    sol = Solution()
    result = sol.purchasePlans(nums, target)
    print(result)