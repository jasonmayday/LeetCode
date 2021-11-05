from queue import Queue


class BinaryTree(object):
    def __init__(self, data):
        self.left = None  ## 左子节点数据
        self.right = None  ## 右子节点数据
        self.data = data  ## 节点的值

    '''插入元素'''
    def insert(self, value):
        node = BinaryTree(value)  ## 添加一个元素即添加一个节点
        if self.data:
            if value <= self.data:  ## 如果插入的数据小于或等于当前节点的数据，插入到左子节点
                if self.left:  ## 如果左子节点存在数据，继续遍历左子节点的左子节点
                    self.left.insert(value)
                else:  ## 如果左子节点不存在数据，则把当前元素插入到该左子节点
                    self.left = node

            else:  ## 如果插入的数据大于当前节点数据，插入到右子节点
                if self.right:  ## 如果右子节点存在数据，继续遍历右子节点的右子节点
                    self.right.insert(value)
                else:  ## 如果右子节点不存在数据，则把当前元素插入到该右子节点
                    self.right = node
        else:
            self.data = value
    
    ## 前序遍历
    def preorder_traversal(self, root):
        preorder_traversal_list = []
        if root:
            preorder_traversal_list.append(root.data)
            preorder_traversal_list += self.preorder_traversal(root.left)
            preorder_traversal_list += self.preorder_traversal(root.right)

        return preorder_traversal_list

    ## 使用栈进行前序遍历（使用列表模拟栈）
    def preorder_traversal_stack(self,root):
        stack = []
        preorder_traversal_stack_list = []
        while stack != [] or root:
            while root:
                stack.append(root)
                preorder_traversal_stack_list.append(root.data)
                root = root.left
            if stack != []:
                root = stack.pop()
                root = root.right
        return preorder_traversal_stack_list

    ## 中序遍历
    def midorder_traversal(self,root):
        midorder_traversal_list = []
        if root:
            midorder_traversal_list = self.midorder_traversal(root.left)
            midorder_traversal_list.append(root.data)
            midorder_traversal_list += self.midorder_traversal(root.right)
        return midorder_traversal_list

    ## 后序遍历
    def postorder_traversal(self,root):
        postorder_traversal_list = []
        if root:
            postorder_traversal_list = self.postorder_traversal(root.left)
            postorder_traversal_list += self.postorder_traversal(root.right)
            postorder_traversal_list.append(root.data)
        return postorder_traversal_list

    ## 层序遍历(层序遍历需要用到队列，不需要用到栈，所以不能用递归实现)
    def levelorder_traversal(self,root):
        levelorder_traversal_list = []
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            root = queue.get()
            levelorder_traversal_list.append(root.data)
            if root.left:
                queue.put(root.left)
            if root.right:
                queue.put(root.right)
        return levelorder_traversal_list

if __name__ == '__main__':
    binaryTree = BinaryTree(12)
    binaryTree.insert(13)
    binaryTree.insert(3)
    binaryTree.insert(6)
    binaryTree.insert(20)
    binaryTree.insert(2)
    preorder_traversal_list = binaryTree.preorder_traversal(binaryTree)
    print("前序遍历结果：{}".format(preorder_traversal_list))
    preorder_traversal_stack_list = binaryTree.preorder_traversal_stack(binaryTree)
    print("使用栈实现前序遍历结果：{}".format(preorder_traversal_stack_list))
    midorder_traversal_list = binaryTree.midorder_traversal(binaryTree)
    print("中序遍历结果：{}".format(midorder_traversal_list))
    postorder_traversal_list = binaryTree.postorder_traversal(binaryTree)
    print("后序遍历结果：{}".format(postorder_traversal_list))
    levelorder_traversal_list = binaryTree.levelorder_traversal(binaryTree)
    print("层序遍历结果：{}".format(levelorder_traversal_list))
