

'''单链表的结点'''
class ListNode:   # 节点类
    def __init__(self, val = 0, next = None):  # 初始化节点
        self.val = val     # val存放数据元素
        self.next = next   # 保存当前节点中下一个节点的引用
        # 每个节点包含两个部分，一部分存放数据变量的val，另一部分存放下一个节点的位置信息next。

'''单链表'''
class SingleLinkedList():
    def __init__(self):   # 初始化链表
        self.head = None  # 先初始化一个头节点为空

    '''展示功能'''
    # 判断链表是否为空
    def is_empty(self):
        return not self.head  # if self.head is None: return Ture.

    # 获取链表的长度
    def length(self):
        cur = self.head        # 初始指针，用来移动遍历节点，指向head
        count = 0              # count记录节点数量
        while cur is not None: # 指针指向 None 时表示到达尾部
            count += 1         # 指针后移
            cur = cur.next
        return count

    # 展示链表
    def display(self):
        cur = self.head.next          # 定位到第一个节点
        for i in range(self.length):  # 根据长度判断是否到末尾
            print(cur.val)            # 输出节点数据
            cur = cur.next            # 指向下一节点

    '''添加节点'''
    # 在链表的头部添加元素
    def add_first(self, val):
        node = ListNode(val)        # 创建一个新节点
        node.next = self.head   # 新节点指针指向原头部节点
        self.head = node        # 头部节点指针修改为新节点
    
    # 在链表的尾部添加元素
    def add_last(self, val):
        node = ListNode(val)       # 创建一个新节点
        if self.is_empty():    # 先判断是否为空链表
            self.head = node   # 空链表，head 指向新节点
        else:
            cur = self.head    # 不是空链表：
            while cur.next is not None:  # 遍历到最后一个节点
                cur = cur.next
            cur.next = node              # 创建新节点并连接到最后

    # 在指定位置添加元素 
    def add(self, index, val):
        if index < 0:                      # 如果位置在0或者之前，调用头插法
            self.add_first(val)
        elif index > self.length() - 1:    # 如果位置在原链表长度之后，调用尾插法
            self.add_last(val)
        else:
            cur = self.head
            count = 0
            while count < index - 1:
                count += 1
                cur = cur.next
            newest = ListNode(val)
            newest.next = cur.next
            cur.next = newest

    '''删除节点'''
    # 删除头结点
    def delete_head(self):
        cur = self.head
        if self.head is not None:
            self.head = self.head.next
            cur.next = None
        return cur

    # 删除尾节点
    def delete_tail(self):
        cur = self.head
        if self.head is not None:
            if self.head.next is None:  # 如果头结点是唯一的节点
                self.head = None
            else:
                while cur.next.next is not None:
                    cur = cur.next
                cur.next, cur = (None, cur.next)
        return cur

    # 删除指定结点
    def delete_node(self, val):
        cur = self.head  # 指针指向的结点
        pre = None       # 指针指向结点的前一个
        if self.head == val:              # 找到指定元素
            self.head.next = self.head    
        else:
            while cur.val is not val:
                pre = cur                 
                cur = cur.next            # 继续按链表后移节点
            pre.next = cur.next           # 将删除位置前一个节点的next指向删除位置的后一个节点

    '''修改节点'''
    # 修改指定位置的元素
    def modify(self, index, val):
        cur = self.head
        if index < 0 or index > self.length():
            return False
        for i in range(index - 1):
            cur = cur.next
        cur.val = val
        return cur

    '''其他功能'''
    # 查找指定结点是否存在
    def search_node_is_exist(self, val):
        cur = self.head
        while cur is not None:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    # 遍历整个链表
    def traversal(self):
        cur = self.head               # 获取head指针
        while cur is not None:        # 循环遍历
            print(cur.val, end = " ") # 返回value
            cur = cur.next            # 指针后移
        print("\n")
     
    # 反转整个链表
    def reverse_list(self):
        cur, prev = self.head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev

'''创建链表'''
def main():
    List1 = SingleLinkedList()
    print("链表是否为空：", List1.is_empty())

    List1.add_first(2)
    List1.add_first(1)
    List1.add_last(3)
    List1.add_last(4)
    List1.add_last(5)

    length_of_list1 = List1.length()
    print("插入节点后，List1 的长度为：", length_of_list1)

    print("遍历并打印整个链表: ")
    List1.traversal()

    print("反转整个链表: ")
    List1.reverse_list()
    List1.traversal()

    print("删除头节点: ")
    List1.delete_head()
    List1.traversal()

    print("删除尾节点: ")
    List1.delete_tail()
    List1.traversal()

    print("在第二个位置插入5: ")
    List1.add(1, 5)
    List1.traversal()

    print("在第-1个位置插入100：")
    List1.add(-1, 100)
    List1.traversal()

    print("在第100个位置插入2：")
    List1.add(100, 2)
    List1.traversal()

    print("删除元素5：")
    List1.traversal()

    print("修改第5个位置的元素为7: ")
    List1.modify(5, 7)
    List1.traversal()

    print("查找元素1:")
    print(List1.search_node_is_exist(1))

if __name__ == "__main__":
    main()