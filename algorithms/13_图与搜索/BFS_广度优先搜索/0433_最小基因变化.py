"""
https://leetcode-cn.com/problems/minimum-genetic-mutation/

一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。

假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。

例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

注意：
    1. 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
    2. 如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
    3. 假定起始基因序列与目标基因序列是不一样的。

示例 1：
    start: "AACCGGTT"
    end:   "AACCGGTA"
    bank: ["AACCGGTA"]
    返回值: 1

示例 2：
    start: "AACCGGTT"
    end:   "AAACGGTA"
    bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    返回值: 2

示例 3：
    start: "AAAAACCC"
    end:   "AACCCCCC"
    bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    返回值: 3

"""
from typing import List

""" BFS """
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)    # 转换为set, in判断只需O(1)时间
        if end not in bank: # 如果最终结果不在基因库中：
            return -1       # 无法实现目标变化，返回 -1。
        change_map = {"A": "CGT",   # 每个基因对应的可变换基因
                      "C": "AGT",
                      "G": "CAT",
                      "T": "CGA",}
        queue = [(start, 0)]    # 初始结点及当前步数
        while queue:            # 用队列实现广度优先
            node, step = queue.pop(0)   # 从初始节点和第 0 步开始
            if node == end:     # 已经到达目标
                return step     # 返回需要的步数

            for i, gene in enumerate(node):    # 当前序列的每一个基因：(下标，基因)
                for change in change_map[gene]:     # 该基因可以改变的方式
                    new = node[:i] + change + node[i+1:] # 改变后的序列
                    if new in bank:                 # 如果该序列在基因库中
                        queue.append((new, step+1)) # 入队，继续广度搜索
                        bank.remove(new)            # 避免重复遍历
        return -1   # 队列空了说明不可达

if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    sol = Solution()
    result = sol.minMutation(start, end, bank)
    print (result)