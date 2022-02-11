"""
https://leetcode-cn.com/problems/o8SXZn/

给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 i 个水缸配备的水桶容量记作 bucket[i]。小扣有以下两种操作：
    升级水桶：选择任意一个水桶，使其容量增加为 bucket[i]+1
    蓄水：将全部水桶接满水，倒入各自对应的水缸

每个水缸对应最低蓄水量记作 vat[i]，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

注意：实际蓄水量 达到或超过 最低蓄水量，即完成蓄水要求。

示例 1：
    输入：bucket = [1,3], vat = [6,8]
    输出：4
    解释：
        第 1 次操作升级 bucket[0]；
        第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。

示例 2：
    输入：bucket = [9,0,1], vat = [0,2,2]
    输出：3
    解释：
        第 1 次操作均选择升级 bucket[1]
        第 2~3 次操作选择蓄水，即可完成蓄水要求。

提示：
    1 <= bucket.length == vat.length <= 100
    0 <= bucket[i], vat[i] <= 10^4

"""

import math
from typing import List

class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        n = len(bucket)
        base = 0                # 可以理解为升级了几次bucket
        for i in range(n):
            if bucket[i] == 0 and vat[i] != 0:  # 若 bucket[i] 为 0，而 vat[i] 不为 0
                base += 1                       # 则必须进行至少一次升级
                bucket[i] = 1

        count = {}              # 每个位置倒满最低蓄水量需要的次数
        for i in range(n):                                  # 遍历所有bucket
            if vat[i] == 0: count[i] = 0                    # 若 vat[i] 为 0，则不需要倒
            else: count[i] = math.ceil(vat[i]/bucket[i])    # 否则计算需要倒几次能达标

        prev = max(count.values()) + base           # 当前至少最少操作次数
        
        while True:                                 # 不断尝试升级水桶
            tmp = max(count.values())               # 当前不考虑base情况下的最大值
            idx = [key for key in count.keys() if count[key] == tmp]    # 找到最大值对应的key，即bucket的位置
            for i in idx:                               # 遍历所有上述位置
                bucket[i] += 1                          # 依次升级水桶
                base += 1
                count[i] = math.ceil(vat[i]/bucket[i])  # 更新count，即需要的次数
            cur = max(count.values()) + base            # 更新过后的最小操作次数
            if prev < cur: break                        # 如果比之前的操作次数还要多，则跳出循环
            prev = cur                                  # 否则，更新prev，再次尝试升级

        return prev

if __name__ == "__main__":
    bucket = [1,3]
    vat = [6,8]
    sol = Solution()
    result = sol.storeWater(bucket, vat)
    print(result)