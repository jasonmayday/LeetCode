'''
https://leetcode-cn.com/problems/same-tree/

给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1：
    输入：p = [1,2,3], q = [1,2,3]
    输出：true

示例 2：
    输入：p = [1,2], q = [1,null,2]
    输出：false

示例 3：
    输入：p = [1,2,1], q = [1,1,2]
    输出：false
 
提示：
    两棵树上的节点数目都在范围 [0, 100] 内
    -10^4 <= Node.val <= 10^4

'''

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p == q
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False

作者：mazheng
链接：https://leetcode-cn.com/problems/same-tree/solution/shen-du-you-xian-bian-li-tong-yong-si-lu-08n7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。