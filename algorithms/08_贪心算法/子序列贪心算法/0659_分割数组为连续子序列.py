"""
https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/

给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：
    输入: [1,2,3,3,4,5]
    输出: True
    解释:
        你可以分割出这样两个连续子序列 : 
        1, 2, 3
        3, 4, 5

示例 2：
    输入: [1,2,3,3,4,4,5,5]
    输出: True
    解释:
        你可以分割出这样两个连续子序列 : 
        1, 2, 3, 4, 5
        3, 4, 5

示例 3：
    输入: [1,2,3,4,4,5]
    输出: False

提示：
    1 <= nums.length <= 10000

"""
from typing import List
from collections import Counter

""" 贪心算法 """
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cntMap = Counter(nums)  # 统计每个数字出现的次数 {3: 2, 4: 2, 5: 2, 1: 1, 2: 1}
        endCntMap = Counter()
        
        for num in nums:        # 访问nums中的各个元素
            if cntMap[num] == 0:
                continue
            cntMap[num] -= 1
            # 存在以 num-1 结尾的长度大于3的子序列
            if endCntMap[num - 1] > 0:
                endCntMap[num - 1] -= 1
                endCntMap[num] += 1
            # 否则，查找后面两个元素拼凑出一个合法序列
            elif cntMap[num + 1] != 0 and cntMap[num + 2] != 0:     
                cntMap[num + 1] -= 1
                cntMap[num + 2] -= 1
                endCntMap[num + 2] += 1
            else:
                return False 
        return True 


""" 贪心算法 """
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        for n in nums:
            for seq in res:
                if n == seq[-1] + 1:    # 如果能接着上一个序列
                    seq.append(n)       # 就在上个序列后添加当前值
                    break               # 直到无法找到比上一个数字大一的数
            else:           # 只有for循环没有break掉才会进入else，也就是说如果没有找到比上一个数字大一的数，才会执行 else 后面的创建新 子数组的步骤
                res.insert(0, [n])      # list.insert(index, obj)
        print (res) # [[3, 4, 5], [1, 2, 3, 4, 5]]
        return all([len(seq) >= 3 for seq in res])  # 最后比较是否所有序列长度大于等于3
    
    
if __name__ == "__main__":
    nums = [1,2,3,3,4,4,5,5]    # [1, 2, 3, 4, 5] [3, 4, 5]
    sol = Solution()
    result = sol.isPossible(nums)
    print (result)