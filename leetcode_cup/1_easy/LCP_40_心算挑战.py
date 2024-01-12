"""
https://leetcode-cn.com/problems/uOAnQW

「力扣挑战赛」心算项目的挑战比赛中，要求选手从 N 张卡牌中选出 cnt 张卡牌，若这 cnt 张卡牌数字总和为偶数，则选手成绩「有效」且得分为 cnt 张卡牌数字总和。
给定数组 cards 和 cnt，其中 cards[i] 表示第 i 张卡牌上的数字。 请帮参赛选手计算最大的有效得分。若不存在获取有效得分的卡牌方案，则返回 0。

示例 1：

    输入：cards = [1,2,8,9], cnt = 3

    输出：18

    解释：选择数字为 1、8、9 的这三张卡牌，此时可获得最大的有效得分 1+8+9=18。

示例 2：

    输入：cards = [3,3,1], cnt = 1

    输出：0

    解释：不存在获取有效得分的卡牌方案。

提示：
    1 <= cnt <= cards.length <= 10^5
    1 <= cards[i] <= 1000

"""
from typing import List

class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        if cnt == 1:            # 如果只选一张卡牌
            max_even = 0        # 初始化最大偶数
            for i in cards:     # 遍历所有卡牌
                if i % 2 == 0 and i > max_even:     # 如果是偶数而且大于之前的最大偶数：
                    max_even = i                    # 更新最大偶数为 i
            return max_even
        
        cards.sort(reverse = True)  # [9,8,2,1]
        score = sum(cards[:cnt])    # score 为最大的 cnt 数字之和
        
        if score % 2 != 0 and len(cards) - cnt >= 1:
            max_odd = -1
            max_even = -1
            for i in range(cnt-1,-1,-1): # 找到前cnt个数中最小的奇数和偶数
                if cards[i] % 2 == 0 and max_even == -1:
                    max_even = cards[i]
                if cards[i] % 2 != 0 and max_odd == -1:
                    max_odd = cards[i]
                if max_odd != -1 and max_even!=-1:
                    break
            min_odd = -1
            min_even = -1
            for i in range(cnt,len(cards)): #找到前cnt个数之后最大的奇数和偶数
                if cards[i] % 2 == 0 and min_even == -1:
                    min_even = cards[i]
                if cards[i] % 2 != 0 and min_odd == -1:
                    min_odd = cards[i]
                if min_even!=-1 and min_odd!=-1:
                    break
            if not(min_odd != -1 and max_even != -1) and not(max_odd != -1 and min_even != -1) :
                # 无法替换数使得和为偶数
                return 0
            if min_odd == -1 or max_even == -1 and not (max_odd == -1 or min_even == -1):
                #只能大偶数换小奇数
                return score - max_odd + min_even
            elif max_odd == -1 or min_even == -1 and not (min_odd == -1 or max_even == -1):
                #只能大奇数换小偶数
                return score - max_even + min_odd
            else:
                #都能换，要比较拿个更划算
                return score - max_even + min_odd if min_odd - max_even > min_even - max_odd else score - max_odd + min_even
        elif score % 2 == 0:
            return score
        else:
            return 0

if __name__ == "__main__":
    cards = [1,2,8,9]
    cnt = 3
    sol = Solution()
    result = sol.maxmiumScore(cards, cnt)
    print(result)