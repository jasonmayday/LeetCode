"""
https://leetcode-cn.com/problems/flatten-nested-list-iterator/

给你一个嵌套的整数列表 nestedList 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。

实现扁平迭代器类 NestedIterator ：
    NestedIterator(List<NestedInteger> nestedList) 用嵌套列表 nestedList 初始化迭代器。
    int next() 返回嵌套列表的下一个整数。
    boolean hasNext() 如果仍然存在待迭代的整数，返回 true ；否则，返回 false 。

你的代码将会用下述伪代码检测：
    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res

如果 res 与预期的扁平化列表匹配，那么你的代码将会被判为正确。

示例 1：
    输入：nestedList = [[1,1],2,[1,1]]
    输出：[1,1,2,1,1]
    解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。

示例 2：
    输入：nestedList = [1,[4,[6]]]
    输出：[1,4,6]
    解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

提示：
    1 <= nestedList.length <= 500
    嵌套列表中的整数值在范围 [-10^6, 10^6] 内

"""
import collections

""" 递归：构造函数中提前「扁平化」整个嵌套列表"""
class NestedIterator(object):
    def dfs(self, nests):
        for nest in nests:
            if nest.isInteger():
                self.queue.append(nest.getInteger())
            else:
                self.dfs(nest.getList())
                    
    def __init__(self, nestedList):
        self.queue = collections.deque()
        self.dfs(nestedList)

    def next(self):
        return self.queue.popleft()

    def hasNext(self):
        return len(self.queue)

""" 迭代：调用 hasNext() 或者 next() 方法的时候扁平化当前的嵌套的子列表"""
class NestedIterator(object):
    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])
        
    def next(self):
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self):
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False
    