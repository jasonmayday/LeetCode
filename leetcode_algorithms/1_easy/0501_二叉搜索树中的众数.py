"""
https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/

给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：
    结点左子树中所含结点的值小于等于当前结点的值
    结点右子树中所含结点的值大于等于当前结点的值
    左子树和右子树都是二叉搜索树

例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2

返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
import collections

# 对于二叉搜索树来说，中序遍历就是一个升序数组，可以基于该数组判断众数。

"""解法2：迭代"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        st = collections.deque()
        cur = root
        pre = None
        maxCount, count = 0, 0
        result = list()
        while cur or st:
            if cur:             # 指针访问节点，一直访问到最底层
                st.append(cur)  # 将节点放入栈内
                cur = cur.left  # 左节点
            else:
                cur = st.pop()  # 中节点
                if pre == None: # 第一个节点
                    count = 1
                elif pre.val == cur.val: # 与前一个节点数值相同
                    count += 1
                else:
                    count = 1
                if count == maxCount:
                    result.append(cur.val)
                if count > maxCount:
                    maxCount = count
                    result = list()
                    result.append(cur.val)
                pre = cur
                cur = cur.right
        return result

"""解法2：递归"""
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.count = 0
        self.maxCount = 0
        self.pre = None
        self.result = list()

        def searchBST(cur: TreeNode):
            if cur == None:                 # 递归函数遇到叶子节点则返回
                return
            searchBST(cur.left)
            if self.pre == None:            # 遍历到根节点，或者说前一个节点不等于当前节点时，开始计数
                self.count = 1
            elif self.pre.val == cur.val:   # 若前一个节点值等于当前节点值，则计数+1
                self.count += 1
            else:
                self.count = 1
            self.pre = cur
                                            # 更新 maxCount 的方式是通过比较当前计数值与最大值
            if self.count == self.maxCount: # 若相等，则在结果中加入当前节点值：
                self.result.append(cur.val)
            if self.count > self.maxCount:  # 若大于最大值，则更新 result 以及 maxCount
                self.maxCount = self.count
                self.result = list()
                self.result.append(cur.val)
            
            searchBST(cur.right)
            return
        
        searchBST(root)
        return self.result

if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    sol = Solution()
    result = sol.findMode(root)
    print(result)
