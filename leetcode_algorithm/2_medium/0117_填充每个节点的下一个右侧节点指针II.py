"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/

给定一个二叉树

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：
    你只能使用常量级额外空间。
    使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

示例：
    输入：root = [1,2,3,4,5,null,7]
    输出：[1,#,2,3,#,4,5,7,#]
    解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。

提示：
    树中的节点数小于 6000
    -100 <= node.val <= 100

"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
    def __str__(self):
        return str(self.val)   

def list_to_binarytree(nums):
    def level(index):
        if index >= len(nums) or nums[index] is None:
            return None
        root = Node(nums[index])
        root.left = level(2 * index + 1)    # 往左递推  # 从根开始一直到最左，直至为空
        root.right = level(2 * index + 2)   # 往右回溯  # 再返回上一个根，回溯右
        return root     # 再返回根
    return level(0)    

def printBFS(root):
    res = []         
    if root is None:
        return
    else:
        queue = [root] # 每次输出一行，所用数据结构为队列
        while queue:
            currentNode = queue.pop(0)   # 弹出元素
            res.append(currentNode.val)  # 打印元素值
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
    return res


from collections import deque

""" 迭代解法1 """
class Solution:
    def connect(self, root):
        if not root:
            return None
        cur = root
        while cur:
            dummyHead = Node(-1)    # 为下一行的之前的节点，相当于下一行所有节点链表的头结点；
            pre = dummyHead
            while cur:
                if cur.left:        # 链接下一行的节点
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummyHead.next    # 此处为换行操作，更新到下一行
        return root


""" 迭代解法2 """
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:    # 注意这里特殊情况的返回要写return root，如果写return [] 显示错误，不是预期的返回类型
            return root
        q = deque()     # 初始化一个队列
        q.append(root)  # 将根节点放入队列中
        while q:        # 当队列不为空时
            m = len(q)  # 首先记录一下当前层的节点的数目，因为需要每层最后一个节点指向NULL
            for i in range(m):      # 将每一层的节点的用next指针连起来
                tmp = q.popleft()   # 首先将队列中的第一个节点弹出
                if i < m - 1:       # 如果此时next连接不是最后一个节点，则将当前弹出节点的next指向队列中的第一个节点。因为初始状态每个节点的next均指向NULL，所以这边不需要特殊处理每层的最后一个节点
                    tmp.next = q[0]
                if tmp.left:            # 注意这里虽然题目是完美二叉树，但可能是最后一层，还是需要判断一下
                    q.append(tmp.left)  # 如果有左子树，放入队列中
                if tmp.right:           # 如果有右子树，放入队列中
                    q.append(tmp.right)      
        return root     # 因为是对root中的点进行连接修改的，在内存地址上就是跟着变的，所以直接返回root即可。（这个地方不知道这么理解对不对，也没找到确定的答案，请大家指导啊，官方题解下面也有人问这个问题，但是还没有回复。）


if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,4,5,None,7])
    sol = Solution()
    result = sol.connect(root)
    print (printBFS(result))