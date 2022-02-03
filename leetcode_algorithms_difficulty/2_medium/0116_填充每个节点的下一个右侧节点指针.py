"""
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

示例 1：
    输入：root = [1,2,3,4,5,6,7]
    输出：[1,#,2,3,#,4,5,6,7,#]
    解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

示例 2:
    输入：root = []
    输出：[]

提示：
    树中节点的数量在 [0, 2^12 - 1] 范围内
    -1000 <= node.val <= 1000

进阶：
    你只能使用常量级额外空间。
    使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。

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

""" 迭代解法一 """
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        queue = [root]
        while queue:
            size = len(queue)
            # 将队列中的元素串联起来
            tmp = queue[0]
            for i in range(1,size):
                tmp.next = queue[i]
                tmp = queue[i]
            for _ in range(size):           # 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
                tmp = queue.pop(0)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
        return root

""" 迭代解法二 """
class Solution(object):
    def connect(self, root):
        if not root:
            return root
        leftmost = root         # 从根节点开始
        while leftmost.left:    # 循环条件是当前节点的left不为空，当只有根节点或所有叶子节点都出串联完后循环就退出了
            tmp = leftmost
            while tmp:      # 利用 tmp 的信息串联节点
                tmp.left.next = tmp.right   # 将 tmp 的左右节点都串联起来（两个串联的节点都有一个共同的父节点）（外层循环已经判断了当前节点的 left 不为空）
                if tmp.next:                # 下一个不为空说明上一层已经帮我们完成串联了
                    tmp.right.next = tmp.next.left  # 再次串联（两个串联的节点的父节点不同，通过父节点的next找到邻居，完成串联）
                tmp = tmp.next  # 继续右边遍历
            leftmost = leftmost.left      # 从下一层的最左边开始遍历
        return root


""" 递归 """
class Solution(object):
    def connect(self, root):
        def dfs(root):
            if not root:
                return
            left = root.left
            right = root.right
            while left:     # 配合动画演示理解这段，以root为起点，将整个纵深这段串联起来
                left.next = right
                left = left.right
                right = right.left
            
            dfs(root.left)  # 递归的调用左右节点，完成同样的纵深串联
            dfs(root.right)
        dfs(root)
        return root


if __name__ == "__main__":
    root = list_to_binarytree([1,2,3,4,5,6,7])
    sol = Solution()
    result = sol.connect(root)
    print (printBFS(result))