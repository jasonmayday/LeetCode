"""
https://leetcode.cn/problems/validate-stack-sequences/

给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 true；否则，返回 false 。

示例 1：
    输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    输出：true
    解释：我们可以按以下顺序执行：
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
    输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
    输出：false
    解释：1 不能在 2 之前弹出。

提示：
    1 <= pushed.length <= 1000
    0 <= pushed[i] <= 1000
    pushed 的所有元素 互不相同
    popped.length == pushed.length
    popped 是 pushed 的一个排列

"""
from typing import List

""" 方法一：栈模拟
    遍历两个数组，模拟入栈和出栈操作"""
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for x in pushed:    # 遍历数组 pushed，
            stack.append(x) # 将 pushed 的每个元素依次入栈；
            # print (stack)
            while stack and stack[-1] == popped[j]: # 每次将 pushed 的元素入栈之后，如果栈不为空, 且栈顶元素与 popped 的当前元素相同
                stack.pop()                         # 则将栈顶元素出栈，
                j += 1
        return len(stack) == 0

if __name__ == "__main__":
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]
    sol = Solution()
    result = sol.validateStackSequences(pushed, popped)
    print(result)