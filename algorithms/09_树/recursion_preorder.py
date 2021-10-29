'''
       1
     ↙   ↘
   2       3
 ↙  ↘    ↙  ↘
4    5   6    7
                ↘
                  8
'''

class Node(object):
    def __init__ (self, value):
        self.value = value # 节点的数值
        self.left = None   # left默认设置是None
        self.right = None  # right默认设置是None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)   # 当传递一个根节点，调用类 node 的构造函数（__init__ 函数）时，会创建二叉树

    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        else:
            print('traversal type' + str(traversal_type) + 'is not supported')
            return False

    def preorder_print(self, start, traversal):                     # Traversal 是打印在屏幕上的字符串，每次都会更新
        """root --> left --> right"""
        if start:                                                   # 检查当前节点是否为空
            traversal += (str(start.value) + "-" )                  # 递归函数里先处理根节点，起始值和遍历字符串每次都会更新
            traversal = self.preorder_print(start.left, traversal)  # 递归处理左子树，递归调用前序函数
            traversal = self.preorder_print(start.right, traversal) # 递归处理右子树，递归调用前序函数，此行仅在左子树不存在时才有效
        return traversal                                            # 遍历将包含一个字符串
    


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left =Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree("preorder"))      