"""
https://leetcode-cn.com/problems/can-place-flowers/

假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组  flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

示例 1：
    输入：flowerbed = [1,0,0,0,1], n = 1
    输出：true

示例 2：
    输入：flowerbed = [1,0,0,0,1], n = 2
    输出：false

提示：
    1 <= flowerbed.length <= 2 * 10^4
    flowerbed[i] 为 0 或 1
    flowerbed 中不存在相邻的两朵花
    0 <= n <= flowerbed.length

"""
from typing import List

""" 因为连续三个0，就可以种花，但是在前端和末尾有 2 个 0 就可以，比如[0,0,1,0,0]
    那么在最前面和最后面各加一个0，就不用考虑边界条件
    """
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        flowerbed = [0] + flowerbed + [0]   # 在最前面和最后面加一个 0，而不是分情况讨论数组长度
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count = count + 1
            if count >= n:
                return True
        return False
        
if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 2
    sol = Solution()
    result = sol.canPlaceFlowers(flowerbed, n)
    print(result)