"""
https://leetcode-cn.com/problems/escape-a-large-maze/

在一个 10^6 x 10^6 的网格中，每个网格上方格的坐标为 (x, y) 。

现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。

每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。

只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。

示例 1：
    输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
    输出：false
    解释：
    从源方格无法到达目标方格，因为我们无法在网格中移动。
    无法向北或者向东移动是因为方格禁止通行。
    无法向南或者向西移动是因为不能走出网格。

示例 2：
    输入：blocked = [], source = [0,0], target = [999999,999999]
    输出：true
    解释：
    因为没有方格被封锁，所以一定可以到达目标方格。

提示：
    0 <= blocked.length <= 200
    blocked[i].length == 2
    0 <= xi, yi < 10^6
    source.length == target.length == 2
    0 <= sx, sy, tx, ty < 10^6
    source != target
    题目数据保证 source 和 target 不在封锁列表内

"""
from typing import List
from collections import deque

"""方法一：有限步数的广度优先搜索 BFS"""
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:

        BLOCKED = -1    # BLOCKED: 在包围圈中
        VALID = 0       # VALID:   不在包围圈中
        FOUND = 1       # FOUND:   无论在不在包围圈中，但在 n(n-1)/2 步搜索的过程中经过了 target
        BOUNDARY = 10 ** 6

        if len(blocked) < 2:
            return True

        hash_blocked = set(tuple(pos) for pos in blocked)

        def check(start: List[int], finish: List[int]) -> int:
            sx, sy = start
            fx, fy = finish
            countdown = len(blocked) * (len(blocked) - 1) // 2
            
            q = deque([(sx, sy)])
            visited = set([(sx, sy)])
            
            while q and countdown > 0:
                x, y = q.popleft()
                for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= nx < BOUNDARY and 0 <= ny < BOUNDARY and (nx, ny) not in hash_blocked and (nx, ny) not in visited:
                        if (nx, ny) == (fx, fy):
                            return FOUND
                        countdown -= 1
                        q.append((nx, ny))
                        visited.add((nx, ny))
            
            if countdown > 0:
                return BLOCKED
            return VALID

        if (result := check(source, target)) == FOUND:
            return True
        elif result == BLOCKED:
            return False
        else:
            result = check(target, source)
            if result == BLOCKED:
                return False
            return True

"""方法二：离散化 + 广度优先搜索"""
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) < 2:
            return True
            
        BOUNDARY = 10**6

        # 离散化
        rows = sorted(set(pos[0] for pos in blocked) | {source[0], target[0]})
        columns = sorted(set(pos[1] for pos in blocked) | {source[1], target[1]})
        r_mapping, c_mapping = dict(), dict()
        

        r_id = (0 if rows[0] == 0 else 1)
        r_mapping[rows[0]] = r_id
        for i in range(1, len(rows)):
            r_id += (1 if rows[i] == rows[i - 1] + 1 else 2)
            r_mapping[rows[i]] = r_id
        if rows[-1] != BOUNDARY - 1:
            r_id += 1

        c_id = (0 if columns[0] == 0 else 1)
        c_mapping[columns[0]] = c_id
        for i in range(1, len(columns)):
            c_id += (1 if columns[i] == columns[i - 1] + 1 else 2)
            c_mapping[columns[i]] = c_id
        if columns[-1] != BOUNDARY - 1:
            c_id += 1

        grid = [[0] * (c_id + 1) for _ in range(r_id + 1)]
        for x, y in blocked:
            grid[r_mapping[x]][c_mapping[y]] = 1
        
        sx, sy = r_mapping[source[0]], c_mapping[source[1]]
        tx, ty = r_mapping[target[0]], c_mapping[target[1]]

        q = deque([(sx, sy)])
        grid[sx][sy] = 1
        while q:
            x, y = q.popleft()
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= nx <= r_id and 0 <= ny <= c_id and grid[nx][ny] != 1:
                    if (nx, ny) == (tx, ty):
                        return True
                    q.append((nx, ny))
                    grid[nx][ny] = 1
        
        return False

if __name__ == "__main__":
    blocked = [[0,1],[1,0]]
    source = [0,0]
    target = [0,2]
    sol = Solution()
    result = sol.isEscapePossible(blocked, source, target)
    print(result)