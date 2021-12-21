"""
https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/

给你一个整数数组 arr，只有可以将其划分为三个和相等的 非空 部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i + 1 < j 且满足 (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1]) 就可以将数组三等分。

示例 1：
    输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    输出：true
    解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
    输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    输出：false

示例 3：
    输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
    输出：true
    解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

提示：
    3 <= arr.length <= 5 * 10^4
    -10^4 <= arr[i] <= 10^4

"""
from typing import List

''' 方法1：暴力解法，两重循环
    循环第一部分终点i，第二部分终点j
    累加 [0,i], [i,j], [j,n] '''

'''方法2'''
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:  # 我们要将数组平均分成三分，那么每一份的和一定是sum(A)/3
            return False
        cur = count = 0
        for a in A:
            cur += a
            if cur == total // 3:
                count += 1
                cur = 0
        return count >= 3
    
'''方法3：双指针'''
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:  # 我们要将数组平均分成三分，那么每一份的和一定是sum(A)/3
            return False
        
        left, right = 0, len(A)-1
        leftSum, rightSum = A[left], A[right]

        while left + 1 < right:     # left + 1 < right: 防止将数组只分成两部分，中间部分至少要有一个元素
            # 左右都等于total/3，中间肯定等于total/3
            if leftSum == total/3 and rightSum == total/3:
                return True
            if leftSum != total/3:
                left += 1
                leftSum += A[left]
            if rightSum != total/3:
                right -= 1
                rightSum += A[right]
        return False

if __name__ == "__main__":      
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    sol = Solution()
    result = sol.canThreePartsEqualSum(arr)
    print(result)