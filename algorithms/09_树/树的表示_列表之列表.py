'''

在“列表之列表”的树中，我们将根节点的值作为列表的第一个元素；
第二个元素是代表左子树的列表；
第三个元素是代表右子树的列表。

可以通过标准的列表切片操作访问子树。树的根节点是myTree[0]，左子树是myTree[1]，右子树是myTree[2]。
'''

def BinaryTree(r):
    return [r, [], []]

'''插入左子树'''
def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root

'''插入右子树'''
def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root

'''树的访问函数'''
def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)

insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l = getLeftChild(r)
setRootVal(l,9)
insertLeft(l,11)
getRightChild(getRightChild(r))