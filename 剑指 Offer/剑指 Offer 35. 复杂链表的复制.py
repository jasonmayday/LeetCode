"""
https://leetcode-cn.com/problems/copy-list-with-random-pointer/

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
    val：一个表示 Node.val 的整数。
    random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。

你的代码 只 接受原链表的头节点 head 作为传入参数。

示例 1：
    输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
    输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
    输入：head = [[1,1],[2,1]]
    输出：[[1,1],[2,1]]

示例 3：
    输入：head = [[3,null],[3,0],[3,null]]
    输出：[[3,null],[3,0],[3,null]]

提示：
    0 <= n <= 1000
    -10^4 <= Node.val <= 10^4
    Node.random 为 null 或指向链表中的节点。

"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

""" 如果没有random，直接复制过来就完事了，
    但是由于有random，它会随机指向下一个，但是如果此时被随机指向的那个节点还没有生成，就无法指向。
    所以先利用哈希表把所有节点先拷贝一遍，然后在挨个取出来连接一下。"""

""" 解法1"""
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        p = head
        
        ''' 第1步，在每个原节点后面创建一个新节点 '''
        while p:
            new_node = Node(p.val,None,None)
            new_node.next = p.next
            p.next = new_node
            p = new_node.next
        p = head        # 1 -> 1' -> 2 -> 2' -> 3 -> 3'
        
        ''' 第2步，设置新节点的随机节点'''
        while p:
            if p.random:
                p.next.random = p.random.next   # 比如 原节点1的随机指针指向原节点3，新节点1的随机指针指向的是原节点3的next
            p = p.next.next                     # 也就是，原节点i的随机指针(如果有的话)，指向的是原节点j；那么新节点i的随机指针，指向的是原节点j的next
        
        ''' 第3步，将两个链表分离'''
        p = head
        dummy = Node(-1,None,None)
        cur = dummy
        while p:
            cur.next = p.next
            cur = cur.next
            p.next = cur.next
            p = p.next
        return dummy.next


""" 解法2：哈希表 """
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        # 创建一个哈希表，key是原节点，value是新节点    
        d = dict()
        p = head
        # 将原节点和新节点放入哈希表中
        while p:
            new_node = Node(p.val,None,None)
            d[p] = new_node
            p = p.next
        p = head
        # 遍历原链表，设置新节点的next和random
        while p:
            # p是原节点，d[p]是对应的新节点，p.next是原节点的下一个
            # d[p.next]是原节点下一个对应的新节点
            if p.next:
                d[p].next = d[p.next]
            # p.random是原节点随机指向
            # d[p.random]是原节点随机指向  对应的新节点    
            if p.random:
                d[p].random = d[p.random]
            p = p.next
        # 返回头结点，即原节点对应的value(新节点)
        return d[head]

