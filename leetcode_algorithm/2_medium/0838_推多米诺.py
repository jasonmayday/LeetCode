"""
https://leetcode-cn.com/problems/push-dominoes/

n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：
    dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
    dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
    dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。

返回表示最终状态的字符串。

示例 1：
    输入：dominoes = "RR.L"
    输出："RR.L"
    解释：第一张多米诺骨牌没有给第二张施加额外的力。

示例 2：
    输入：dominoes = ".L.R...LR..L.."
    输出："LL.RR.LLRRLL.."

提示：
    n == dominoes.length
    1 <= n <= 10^5
    dominoes[i] 为 'L'、'R' 或 '.'

"""

""" 方法1：模拟
    枚举所有连续的没有被推动的骨牌，根据这段骨牌的两边骨牌（如果有的话）的推倒方向决定这段骨牌的最终状态
    使用两个指针 ii 和 jj 来枚举所有连续的没有被推动的骨牌，left 和 right 表示两边骨牌的推倒方向。根据上述三种情况来计算骨牌的最终状态。
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = list(dominoes)
        n = len(s)
        i = 0
        left = 'L'
        while i < n:
            j = i
            while j < n and s[j] == '.':  # 找到一段连续的没有被推动的骨牌
                j += 1
            right = s[j] if j < n else 'R'
            
            if left == right:                   # 如果 "没有被推动的骨牌" 的两边的骨牌同向，那么这段连续的竖立骨牌会倒向同一方向。
                while i < j:
                    s[i] = right
                    i += 1
            
            elif left == 'R' and right == 'L':  # 如果 "没有被推动的骨牌" 的两边的骨牌相对，那么这段骨牌会向中间倒。
                k = j - 1
                while i < k:
                    s[i] = 'R'
                    s[k] = 'L'
                    i += 1
                    k -= 1
            left = right
            i = j + 1
        return ''.join(s)

""" 替换 """
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        od = ""
        while dominoes != od:
            od = dominoes     # replace(old, new)
            dominoes = dominoes.replace("R.L", "T") # 要保护 "R.L" 避免因为其他规则影响，每次出现R.L修改需要标记其发生变化
            dominoes = dominoes.replace(".L", "LL") # 向左倒
            dominoes = dominoes.replace("R.", "RR") # 向右倒
            dominoes = dominoes.replace("T", "R.L") # 恢复 "R.L"
        return dominoes

if __name__ == "__main__":
    dominoes = ".L.R...LR..L.."
    sol = Solution()
    result = sol.pushDominoes(dominoes)
    print (result) 