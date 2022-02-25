"""
https://leetcode-cn.com/problems/nim-game/

你和你的朋友，两个人一起玩 Nim 游戏：
    桌子上有一堆石头。
    你们轮流进行自己的回合，你作为先手。
    每一回合，轮到的人拿掉 1 - 3 块石头。
    拿掉最后一块石头的人就是获胜者。

假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 n 的情况下赢得游戏。如果可以赢，返回 true；否则，返回 false 。

示例 1：
    输入：n = 4
    输出：false
    解释：如果堆中有 4 块石头，那么你永远不会赢得比赛；
         因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。

示例 2：
    输入：n = 1
    输出：true

示例 3：
    输入：n = 2
    输出：true

提示：
    1 <= n <= 2^31 - 1

"""
"""
解法：博弈论

首先，若一个游戏满足：
    由两名玩家交替行动
    在游戏进行的任意时刻，可以执行的合法行动与轮到哪位玩家无关
    不能行动的玩家判负

则称该游戏为一个公平组合游戏。

尼姆游戏（NIM）属于公平组合游戏，但常见的棋类游戏，比如围棋就不是公平组合游戏，因为围棋交战双方分别只能落黑子和白子，胜负判定也比较复杂，不满足条件 2 和 3 。

其次，我们介绍必胜状态和必败状态两个名词：
    必胜状态：先手进行某一个操作，留给后手是一个必败状态时，对于先手来说是一个必胜状态。即先手可以走到某一个必败状态。
    必败状态：先手无论如何操作，留给后手都是一个必胜状态时，对于先手来说是一个必败状态。即先手走不到任何一个必败状态。

本题的结论为：
    假设共有 nn 块石头，如果 nn 是 44 的倍数，先手必败；否则先手必胜。

证明：
    如果 n 是 4 的倍数，那么必可以表示为 n = 4k (k ∈ N+) 的形式。那么无论先手选择取走 1,2,3 块石头，后手都可以对应地取走 3,2,1 块石头，从而将总石头数量变为 n′ = 4(k−1)
    那么，按照上述方式，先手和后手各取 k 轮后，后手的最后一次操作完成后，总石头数量变为 0，此时先手不能行动，必败。

综上所述，如果石头数量 nn 是 44 的倍数，那么此时对先手来讲为必败状态。
    如果 n 不是 4 的倍数，那么必可以表示为 n = 4k + r (k ∈ N+, r ∈ [1,2,3]) 的形式（其中 r 为 n 模 4 的余数）。
    此时，先手第一步取刚好 r 块石头，就可以让后手面临 n 为 4 的倍数的必败状态，所以根据我们上面的定义，这种情况下，先手为必胜状态。

"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.canWinNim(n)
    print (result)