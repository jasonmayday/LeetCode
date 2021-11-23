"""
堆的特点：
    1. 内部数据是有序的
    2. 可以弹出堆顶的元素，大顶堆就是弹出最大值，小顶堆就是弹出最小值
    3. 每次加入新元素或者弹出堆顶元素后，调整堆使之重新有序仅需要O(logn)的时间
    4. 支持在线算法

堆的本质：
    1.  它是一个完全二叉树
    2.  实现的时候我们不需要建造一个树，改用一个数组即可
        那么我们是如何把一个完全二叉树和一个数组关联到一起的呢？
        给树的节点编号，节点的编号就是元素在数组中的下标
    3.  于是我们发现一个很重要的结论：
        已知一个节点的编号为index，那么它的父节点的编号为：
        father_index = (index - 1) / 2
        左孩子节点的编号为
        left_index = index ∗ 2 + 1
        右孩子节点的编号为
        right_index = index ∗ 2 + 2


"""


class Heap:
    """初始化"""
    def __init__(self,desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc
    
    @property
    def size(self):
        """堆的大小"""
        return len(self.heap)
    
    """返回堆顶元素"""
    def top(self):
        if self.size:
            return self.heap[0]
        return None
    
    """添加元素"""
    def push(self,item):
        """
        第一步，把元素加入到数组末尾
        第二步，把末尾元素向上调整
        """
        self.heap.append(item)
        self._sift_up(self.size-1)
    
    def pop(self):
        """
        弹出堆顶
        第一步，记录堆顶元素的值
        第二步，交换堆顶元素与末尾元素
        第三步，删除数组末尾元素
        第四步，新的堆顶元素向下调整
        第五步，返回答案
        """
        item = self.heap[0]
        self._swap(0,self.size-1)
        self.heap.pop()
        self._sift_down(0)
        return item
    
    def _smaller(self,lhs,rhs):
        return lhs > rhs if self.desc else lhs < rhs
    
    def _sift_up(self,index):
        """
        向上调整
        如果父节点和当前节点满足交换的关系
        （对于小顶堆是父节点元素更大，对于大顶堆是父节点更小），
        则持续将当前节点向上调整
        """
        while index:
            parent = (index-1) // 2
            
            if self._smaller(self.heap[parent],self.heap[index]):
                break
                
            self._swap(parent,index)
            index = parent
    
    def _sift_down(self,index):
        """
        向下调整
        如果子节点和当前节点满足交换的关系
        （对于小顶堆是子节点元素更小，对于大顶堆是子节点更大），
        则持续将当前节点向下调整
        """
        # 若存在子节点
        while index*2+1 < self.size:
            smallest = index
            left = index*2+1
            right = index*2+2
            
            if self._smaller(self.heap[left],self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right],self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index,smallest)
            index = smallest
    
    """交换两个元素"""
    def _swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = Heap()
        self.k = k
        for num in nums:
            self.heap.push(num)
            if self.heap.size > k:
                self.heap.pop()


    def add(self, val: int) -> int:
        self.heap.push(val)
        if self.heap.size > self.k:
            self.heap.pop()
        return self.heap.top()

