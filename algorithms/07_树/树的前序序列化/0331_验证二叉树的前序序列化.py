"""
https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/

序列化二叉树的一种方法是使用 前序遍历 。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

保证 每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。

你可以认为输入格式总是有效的
    例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

注意：不允许重建树。

示例 1:
    输入: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    输出: true

示例 2:
    输入: preorder = "1,#"
    输出: false

示例 3:
    输入: preorder = "9,#,#,1"
    输出: false

提示:
    1 <= preorder.length <= 10^4
    preorder 由以逗号 “，” 分隔的 [0,100] 范围内的整数和 “#” 组成

"""

""" 方法一：栈 """
class Solution(object):
    def isValidSerialization(self, preorder):
        stack = []
        for node in preorder.split(','):
            stack.append(node)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop(), stack.pop(), stack.pop()   # 当遇到 "x,#,#" 的时候，说明 "x" 是子节点，弹出 "x,#,#"
                stack.append('#')                       # 加入 #，相当于把 "x,#,#" 变为 "#"
        return len(stack) == 1 and stack.pop() == '#'   # 当栈中只剩一个元素，并且为 "#"时，说明字符串是有效的前序遍历

""" 方法二：计算入度出度
    树（甚至图）中，所有节点的入度之和等于出度之和"""
class Solution(object):
    def isValidSerialization(self, preorder):
        nodes = preorder.split(',')
        diff = 1                # diff = 出度 - 入度
        for node in nodes:
            diff -= 1           # 每个空节点（ "#" ）会提供 0 个出度和 1 个入度。
            if diff < 0:        #
                return False    # 在遍历到任何一个节点的时候，要求diff >= 0
            if node != '#':     # 每个非空节点会提供 2 个出度和 1 个入度（根节点的入度是 0）。
                diff += 2
        return diff == 0

if __name__ == "__main__":
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    sol = Solution()
    result = sol.isValidSerialization(preorder)
    print (result)