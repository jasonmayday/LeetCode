"""
https://leetcode-cn.com/problems/erect-the-fence/

在一个二维的花园中，有一些用 (x, y) 坐标表示的树。
由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。
只有当所有的树都被绳子包围时，花园才能围好栅栏。
你需要找到正好位于栅栏边界上的树的坐标。

示例 1:
    输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
    解释:

示例 2:
    输入: [[1,2],[2,2],[4,2]]
    输出: [[1,2],[2,2],[4,2]]
    解释:

即使树都在一条直线上，你也需要先用绳子包围它们。

注意:
    1. 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
    2. 输入的整数在 0 到 100 之间。
    3. 花园至少有一棵树。
    4. 所有树的坐标都是不同的。
    5. 输入的点没有顺序。输出顺序也没有要求。

"""
from typing import List

""" 方法一: Jarvis 算法 """
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        leftMost = 0
        for i, tree in enumerate(trees):
            if tree[0] < trees[leftMost][0]:
                leftMost = i

        ans = []
        vis = [False] * n
        p = leftMost
        while True:
            q = (p + 1) % n
            for r, tree in enumerate(trees):
                # // 如果 r 在 pq 的右侧，则 q = r
                if cross(trees[p], trees[q], tree) < 0:
                    q = r
            # 是否存在点 i, 使得 p q i 在同一条直线上
            for i, b in enumerate(vis):
                if not b and i != p and i != q and cross(trees[p], trees[q], trees[i]) == 0:
                    ans.append(trees[i])
                    vis[i] = True
            if not vis[q]:
                ans.append(trees[q])
                vis[q] = True
            p = q
            if p == leftMost:
                break
        return ans

""" 方法二: Graham 算法"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        def distance(p: List[int], q: List[int]) -> int:
            return (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])

        n = len(trees)
        if n < 4:
            return trees

        # 找到 y 最小的点 bottom
        bottom = 0
        for i, tree in enumerate(trees):
            if tree[1] < trees[bottom][1]:
                bottom = i
        trees[bottom], trees[0] = trees[0], trees[bottom]

        # 以 bottom 原点，按照极坐标的角度大小进行排序
        def cmp(a: List[int], b: List[int]) -> int:
            diff = cross(trees[0], b, a) - cross(trees[0], a, b)
            return diff if diff else distance(trees[0], a) - distance(trees[0], b)
        trees[1:] = sorted(trees[1:], key=cmp_to_key(cmp))

        # 对于凸包最后且在同一条直线的元素按照距离从小到大进行排序
        r = n - 1
        while r >= 0 and cross(trees[0], trees[n - 1], trees[r]) == 0:
            r -= 1
        l, h = r + 1, n - 1
        while l < h:
            trees[l], trees[h] = trees[h], trees[l]
            l += 1
            h -= 1

        stack = [0, 1]
        for i in range(2, n):
            # 如果当前元素与栈顶的两个元素构成的向量顺时针旋转，则弹出栈顶元素
            while len(stack) > 1 and cross(trees[stack[-2]], trees[stack[-1]], trees[i]) < 0:
                stack.pop()
            stack.append(i)
        return [trees[i] for i in stack]

""" 方法三: Andrew 算法"""
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def cross(p: List[int], q: List[int], r: List[int]) -> int:
            return (q[0] - p[0]) * (r[1] - q[1]) - (q[1] - p[1]) * (r[0] - q[0])

        n = len(trees)
        if n < 4:
            return trees

        # 按照 x 从小到大排序，如果 x 相同，则按照 y 从小到大排序
        trees.sort()

        hull = [0]  # hull[0] 需要入栈两次，不标记
        used = [False] * n
        # 求凸包的下半部分
        for i in range(1, n):
            while len(hull) > 1 and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                used[hull.pop()] = False
            used[i] = True
            hull.append(i)
        # 求凸包的上半部分
        m = len(hull)
        for i in range(n - 2, -1, -1):
            if not used[i]:
                while len(hull) > m and cross(trees[hull[-2]], trees[hull[-1]], trees[i]) < 0:
                    used[hull.pop()] = False
                used[i] = True
                hull.append(i)
        # hull[0] 同时参与凸包的上半部分检测，因此需去掉重复的 hull[0]
        hull.pop()

        return [trees[i] for i in hull]

if __name__ == "__main__":
    n = 5
    sol = Solution()
    result = sol.findIntegers(n)
    print(result)